import os
import json
import psycopg2
import redis
import time

# Configurações do PostgreSQL
postgres_config = {
    "host": os.getenv("POSTGRES_HOST", "postgres"),
    "database": os.getenv("POSTGRES_DB", "employee"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", "2512"),
}

# Configurações do Redis
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = 6379  # Porta padrão para comunicação interna no Docker

# Função para conectar ao PostgreSQL com tentativas de reconexão
def connect_postgres():
    while True:
        try:
            conn = psycopg2.connect(**postgres_config)
            print("Conectado ao PostgreSQL com sucesso.")
            return conn
        except Exception as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}. Tentando novamente em 5 segundos...")
            time.sleep(5)

def transfer_redis_to_postgres(batch_size=10000):
    conn = None
    cursor = None
    try:
        # Conecta ao PostgreSQL
        conn = connect_postgres()
        cursor = conn.cursor()

        # Conecta ao Redis
        redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        print("Conectado ao Redis com sucesso.")

        # Obtém todas as chaves do Redis
        keys = redis_client.keys("*")
        total_keys = len(keys)
        print(f"{total_keys} registros encontrados no Redis.")

        for i in range(0, total_keys, batch_size):
            batch_keys = keys[i:i + batch_size]  # Seleciona as chaves do lote atual
            batch_data = []

            for key in batch_keys:
                try:
                    data = json.loads(redis_client.get(key))
                    batch_data.append(
                        (data["tipo"], data["nome"], data["preco"], data["unidade"])
                    )
                except Exception as e:
                    print(f"Erro ao processar chave {key}: {e}")

            # Inserir o lote no PostgreSQL
            try:
                cursor.executemany(
                    """
                    INSERT INTO produtos (tipo, nome, preco, unidade)
                    VALUES (%s, %s, %s, %s)
                    """,
                    batch_data
                )
                conn.commit()
                print(f"Lote {i // batch_size + 1} processado com sucesso ({len(batch_data)} registros).")
            except Exception as e:
                conn.rollback()  # Desfaz apenas o lote atual em caso de erro
                print(f"Erro ao inserir lote {i // batch_size + 1}: {e}")

    except Exception as e:
        print(f"Erro ao transferir dados: {e}")

    finally:
        # Garantindo que a conexão e o cursor sejam fechados corretamente
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    transfer_redis_to_postgres()
