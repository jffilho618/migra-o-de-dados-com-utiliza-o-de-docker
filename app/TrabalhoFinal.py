import abc
import random
from datetime import datetime, time
import psycopg2


class Funcionario():
    def __init__(self, usuario, senha):
        self._usuario = usuario
        self._senha = senha
        
class Autenticacao(abc.ABC):
    @abc.abstractmethod
    def login(self, usuario, senha):
        pass

class AutenticacaoSimples:
    def __init__(self):
        self.usuario_padrao = "admin"
        self.senha_padrao = "admin"

    def login(self, funcionario: Funcionario):
        if funcionario._usuario == self.usuario_padrao and funcionario._senha == self.senha_padrao:
            return True
        else:
            return False

Autenticacao.register(AutenticacaoSimples)

def obter_credenciais():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    return Funcionario(usuario, senha)

def autenticar_usuario(autenticacao: Autenticacao):
    funcionario = obter_credenciais()
    if autenticacao.login(funcionario):
        print("Login bem-sucedido!")
        return True
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        return False
    
def autenticacao():
    autenticacao = AutenticacaoSimples()
    tentativas = 3

    while tentativas > 0:
        if autenticar_usuario(autenticacao):
            # menu_historico()
            break
        else:
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")

        if tentativas == 0:
            print("Número máximo de tentativas alcançado!")
            continue



class Produto(abc.ABC):
    def __init__(self, nome, preco, unidade):
        self._nome = nome
        self._preco = preco
        self._unidade = unidade

    @abc.abstractmethod
    def calcular_preco(self, quantidade):
        pass

    @abc.abstractmethod
    def editar(self):
        pass

class Bebidas(Produto):
    def __init__(self, nome, preco, unidade = "UNI"):
        super().__init__(nome, preco, unidade)

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._nome = input("DIGITE O NOVO NOME DA BEBIDA: ").upper()
            self._preco = float(input("DIGITE O NOVO PREÇO DA BEBIDA: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Pastel(Produto):
    def __init__(self, nome, preco, unidade = "UNI"):
        super().__init__(nome, preco, unidade)

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._nome = input("DIGITE O NOVO NOME DO PASTEL: ").upper()
            self._preco = float(input("DIGITE O NOVO PREÇO DO PASTEL: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Acai(Produto):
    def __init__(self, preco, nome):
        super().__init__("AÇAI", preco, "KG")

    def calcular_preco(self, peso):
        return self._preco * (peso / 1000)

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DO AÇAI: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Sorvete(Produto):
    def __init__(self, preco, nome):
        super().__init__("SORVETE", preco, "KG")

    def calcular_preco(self, peso):
        return self._preco * (peso / 1000)

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DO SORVETE: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Cuzcuz(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco, "UNI") 

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DO CUZCUZ: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Massa(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco, 'UNI')

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DA MASSA: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Petisco(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco, 'UNI')

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DO PETISCO: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Pedido:
    def __init__(self, cliente, id_pedido):
        self._cliente = cliente
        self._produtos = []
        self._id_pedido = id_pedido
        now = datetime.now()
        self._data = now.toordinal()  # Convertendo para data Juliana
        self._hora = now.time()  # Armazenando a hora
        self._status = "ABERTO"

    def adicionar_produto(self, produto, quantidade, tipo_produto):
        self._produtos.append((produto, quantidade, tipo_produto))

    def calcular_total(self):
        total = 0
        for produto, quantidade, tipo_produto in self._produtos:
            total += produto.calcular_preco(quantidade)
        return total

    def imprimir_nota(self):
        data_gregoriana = datetime.fromordinal(self._data)  # Convertendo de volta para data Gregoriana
        print("\n")
        print("╔══════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                    NOTA FISCAL                                   ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ ID DO PEDIDO: {self._id_pedido:<65}  ║")
        print(f"║ NOME DO CLIENTE: {self._cliente:<62}  ║")
        print(f"║ DATA DO PEDIDO: {data_gregoriana.strftime('%d/%m/%Y'):<63}  ║")
        print(f"║ HORA DO PEDIDO: {self._hora.strftime('%H:%M:%S'):<63}  ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        for produto, quantidade, tipo_produto in self._produtos:
            if tipo_produto == "AÇAI" or tipo_produto == "SORVETE":
                print(f"║ {tipo_produto:<7} {produto._nome:50} PESO: {quantidade:<4}g  {produto.calcular_preco(quantidade):>5.2f} R$ ║")
            else:
                print(f"║ {tipo_produto:<7} {produto._nome:50} QUANT: {quantidade:<4}  {produto.calcular_preco(quantidade):>5.2f} R$ ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ TOTAL: {self.calcular_total():>70.2f} R$ ║")
        print("╚══════════════════════════════════════════════════════════════════════════════════╝\n")

class Caixa:
    def __init__(self):
        # Configurações do banco de dados
        self.postgres_config = {
            "host": "localhost",  # Ou o IP do servidor, se necessário
            "port": 5410,  # Porta padrão do PostgreSQL
            "database": "employee",  # Nome do banco de dados
            "user": "postgres",  # Nome do usuário
            "password": "2512",  # Senha do banco de dados
        }

    def conectar_bd(self):
        try:
            conn = psycopg2.connect(**self.postgres_config)
            print("Conexão ao banco de dados estabelecida.")
            return conn
        except psycopg2.OperationalError as e:
            print(f"Erro de operação: {e}")
        except psycopg2.DatabaseError as e:
            print(f"Erro no banco de dados: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        return None


    def adicionar_produto(self, produto):
        if produto._preco <= 0:
            print("PREÇO INVÁLIDO! PRODUTO NÃO CADASTRADO!")
            return

        conn = self.conectar_bd()
        print(type(conn))  # Deve exibir <class 'psycopg2.extensions.connection'>

        if conn:
            try:

                with conn.cursor() as cursor:
                    query = """
                        INSERT INTO produtos (tipo, nome, preco, unidade)
                        VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(query, (produto.__class__.__name__.upper(), produto._nome, produto._preco, "uni"))
                    conn.commit()
                    print(f"Produto '{produto._nome}' adicionado ao banco de dados.")
            except Exception as e:
                print(f"Erro ao adicionar produto ao banco de dados: {e}")
            finally:
                conn.close()
            

    def editar_produto(self, nome_produto):
        try:
            for tipo, conteudo in self._produtos.items():                
                if isinstance(conteudo, list):
                    for produto in conteudo:
                        if produto._nome == nome_produto:
                            print("╔═════════════════════════════════════════════════╗")
                            print("║              NOME            ║ PREÇO  ║ UNIDADE ║")
                            print("╠═════════════════════════════════════════════════╣")    
                            print(f"║ {produto._nome:28} ║ {produto._preco:6.2f} ║ {produto._unidade:7} ║")
                            print("╚═════════════════════════════════════════════════╝\n")
                            print("\n1 - EDITAR")
                            print("0 - CANCELAR")
                            try:
                                op = int(input("DIGITE A OPÇÃO DESEJADA: "))
                                if op == 0:
                                    return
                                elif op == 1:
                                    produto.editar()
                                    print(f"{tipo} EDITADO COM SUCESSO!")
                                    return
                                else:
                                    print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                    continue
                            except ValueError:
                                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                continue
                            
           
            print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print(f"Erro: {str(e)}")

    def remover_produto(self, nome_produto):
        try:
            for tipo, lista_produtos in self._produtos.items():
                for produto in lista_produtos:
                    if produto._nome == nome_produto:
                        if tipo == "AÇAI" or tipo == "SORVETE":
                            print("NÃO É POSSÍVEL REMOVER AÇAÍ OU SORVETE!")
                            return
                        print("╔═════════════════════════════════════════════════╗")
                        print("║              NOME            ║ PREÇO  ║ UNIDADE ║")
                        print("╠═════════════════════════════════════════════════╣")    
                        print(f"║ {produto._nome:28} ║ {produto._preco:6.2f} ║ {produto._unidade:7} ║")
                        print("╚═════════════════════════════════════════════════╝\n")
                        print("\n1 - REMOVER")
                        print("0 - CANCELAR")
                        try:
                            op = int(input("DIGITE A OPÇÃO DESEJADA: "))
                            if op == 0:
                                return
                            elif op == 1:
                                lista_produtos.remove(produto)
                                print(f"{tipo} REMOVIDO COM SUCESSO!")
                                return
                            else:
                                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                continue
                        except ValueError:
                            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                            continue
                        
            print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print(f"PRODUTO NÃO ENCONTRADO!")



