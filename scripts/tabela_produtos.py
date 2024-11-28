import psycopg2

# Configurações do PostgreSQL
postgres_config = {
    "host": "localhost",  # Ou o IP do servidor, se necessário
    "port": 5410,  # Porta padrão do PostgreSQL
    "database": "employee",  # Nome do banco de dados
    "user": "postgres",  # Nome do usuário
    "password": "2512",  # Senha do banco de dados
}

# Função para conectar ao PostgreSQL
def connect_postgres():
    try:
        # Conecta ao banco de dados PostgreSQL usando as configurações
        conn = psycopg2.connect(**postgres_config)
        print("Conectado ao PostgreSQL com sucesso.")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

# Função para exibir todas as linhas da tabela 'produtos'
def display_all_rows():
    conn = None
    cursor = None
    try:
        # Conecta ao PostgreSQL
        conn = connect_postgres()
        cursor = conn.cursor()

        # Executa a consulta SELECT para pegar todas as linhas da tabela 'produtos'
        cursor.execute('SELECT * FROM public.produtos;')  # Especificando o esquema 'public'

        # Obtém todos os registros da consulta
        rows = cursor.fetchall()

        # Exibe as linhas
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Erro ao consultar dados: {e}")
    
    finally:
        # Fecha a conexão e o cursor
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# Executa a função para exibir as linhas
if __name__ == "__main__":
    display_all_rows()
