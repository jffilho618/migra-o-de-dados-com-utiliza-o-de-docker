import redis
import json
import uuid
from faker import Faker
import random

# Configuração do Redis
r = redis.StrictRedis(host="localhost", port=6380, db=0, decode_responses=True)

# Gerador de dados falsos
fake = Faker()

# Lista de tipos e unidades possíveis
product_types = ["pastel", "bebida", "petisco"]
units = ["peso", "uni"]

# Função para gerar dados de produtos
def generate_product_data():
    product_id = str(uuid.uuid4())  # ID único
    tipo = random.choice(product_types)
    nome = fake.word().capitalize()
    preco = round(random.uniform(1.0, 100.0), 2)
    unidade = random.choice(units)
    return product_id, {
        "tipo": tipo,
        "nome": nome,
        "preco": preco,
        "unidade": unidade,
    }

# Inserir dados no Redis
def insert_data_redis(num_entries):
    count = 0
    for _ in range(num_entries):
        product_id, data = generate_product_data()
        if not r.exists(product_id):  # Verificar duplicação
            r.set(product_id, json.dumps(data))
            count += 1
    print(f"{count} registros inseridos com sucesso!")

# Inserir 1.000.000 de registros
insert_data_redis(1000000)
