import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from TrabalhoFinal import *

# Classe para a tela de login
class LoginWindow(QtWidgets.QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('ui\login.ui', self)

        self.definir_imagem_voltar()
        self.exibir_imagem_user()

        self.pushButton.clicked.connect(self.fazer_login)
        self.pushButton_2.clicked.connect(self.voltar)

        self.autenticacao = AutenticacaoSimples()

    def definir_imagem_voltar(self):
        voltar_icon = QtGui.QIcon(r'PROJETOS1\21797173-seta-esquerda-icone-isolado-em-branco-fundo-vetor (1).jpg')  
        self.pushButton_2.setIcon(voltar_icon)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))

    def fazer_login(self):
        usuario = self.lineEdit.text()
        senha = self.lineEdit_2.text()

        funcionario = Funcionario(usuario, senha)

        if self.autenticacao.login(funcionario):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos!")

    def voltar(self):
        self.reject()

    def exibir_imagem_user(self):
        pixmap = QtGui.QPixmap(r"PROJETOS1\avatar_15484536.png")
        self.ajustar_imagem(pixmap, self.label)

    def ajustar_imagem(self, pixmap, label):
        if not pixmap.isNull():
            label_width = label.width()
            label_height = label.height()
            pixmap_resized = pixmap.scaled(label_width, label_height, QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)


# Classe principal da interface
class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui\PASTELARIA.ui', self)

        self.caixa = Caixa()

        self.pushButton_4.clicked.connect(self.abrir_relatorio)
        self.pushButton_5.clicked.connect(self.vender_produto)
        self.pushButton_6.clicked.connect(self.editar_produto)

        self.exibir_imagem_user()
        self.exibir_imagen_food()
        self.exibir_imagem_relatorio()


    def exibir_imagem_user(self):
        pixmap = QtGui.QPixmap(r"PROJETOS1\user.png")
        self.ajustar_imagem(pixmap, self.label_6)

    def exibir_imagen_food(self):
        pixmap = QtGui.QPixmap(r"PROJETOS1\fast-food.png")
        self.ajustar_imagem(pixmap, self.label_7)

    def exibir_imagem_relatorio(self):
        pixmap = QtGui.QPixmap(r"PROJETOS1\report.png")
        self.ajustar_imagem(pixmap, self.label_5)

    def ajustar_imagem(self, pixmap, label):
        if not pixmap.isNull():
            label_width = label.width()
            label_height = label.height()
            pixmap_resized = pixmap.scaled(label_width, label_height, QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)

    def inicializar_produtos(self):
        ac = Acai(59, "AÇAI")
        sv = Sorvete(45, "SORVETE")
        misto = Pastel("MISTO", 10.0)
        coca = Bebidas("COCA 350ML", 5)
        porcao = Petisco("BATATA", 15)
        caixa = Caixa()
        ac = Acai(59, "AÇAI")
        sv = Sorvete(45, "SORVETE")
        misto = Pastel("MISTO", 10.0)
        coca = Bebidas("COCA 350ML", 5)
        porcao = Petisco("BATATA", 15)
        carne = Pastel("CARNE", 10)
        frango = Pastel("FRANGO", 10)
        Queijo_presunto = Pastel("QUEIJO E PRESUNTO", 10)
        Queijo_coalho_ou_mussarela = Pastel("QUEIJO COALHO OU MUSSARELA", 10)
        carne_queijo_milho = Pastel("CARNE, QUEIJO E MILHO", 10)
        frango_catupiry_milho = Pastel("FRANGO, CATUPIRY E MILHO", 10)
        queijo_presunto_bacon = Pastel("QUEIJO, PRESUNTO E BACON", 10)
        frango_catupiry = Pastel("FRANGO E CATUPIRY", 10)
        frango_cremoso = Pastel("FRANGO CREMOSO", 12)
        pizza_frango = Pastel("PIZZA DE FRANGO", 12)
        hot_dog = Pastel("HOT DOG", 12)
        Mexicano_Carne = Pastel("MEXICANO DE CARNE", 12)
        Mexicano_frango = Pastel("MEXICANO DE FRANGO", 12)
        Mexicabo_carne_geleia = Pastel("MEXICANO DE CARNE COM GELEIA", 12)
        franbacon = Pastel("FRANBACON", 12)
        xtudao = Pastel("XTUDÃO", 15)
        Big_frango = Pastel("BIG FRANGO", 15)
        Big_Vegetariano = Pastel("BIG VEGETARIANO", 15)
        doce_leite = Pastel("DOCE DE LEITE", 6)
        prestigio = Pastel("PRESTÍGIO", 6)
        nutele = Pastel("NUTELLA", 6)
        Romeu_Julieta = Pastel("ROMEU E JULIETA", 6)
        guarana = Bebidas("GUARANÁ 350ML", 5)
        fanta = Bebidas("FANTA 350ML", 5)
        coca_2l = Bebidas("COCA 2L", 12)
        coca_zero = Bebidas("COCA ZERO 350ML", 5)
        coca_cola_1l = Bebidas("COCA COLA 1L", 8)
        guarana_2l = Bebidas("GUARANÁ 2L", 12)
        fanta_2l = Bebidas("FANTA 2L", 12)
        self.caixa.adicionar_produto(ac)
        self.caixa.adicionar_produto(sv)
        self.caixa.adicionar_produto(misto)
        self.caixa.adicionar_produto(coca)
        self.caixa.adicionar_produto(porcao)
        self.caixa.adicionar_produto(carne)
        self.caixa.adicionar_produto(frango)
        self.caixa.adicionar_produto(Queijo_presunto)
        self.caixa.adicionar_produto(Queijo_coalho_ou_mussarela)
        self.caixa.adicionar_produto(carne_queijo_milho)
        self.caixa.adicionar_produto(frango_catupiry_milho)
        self.caixa.adicionar_produto(queijo_presunto_bacon)
        self.caixa.adicionar_produto(frango_catupiry)
        self.caixa.adicionar_produto(frango_cremoso)
        self.caixa.adicionar_produto(pizza_frango)
        self.caixa.adicionar_produto(hot_dog)
        self.caixa.adicionar_produto(Mexicano_Carne)
        self.caixa.adicionar_produto(Mexicano_frango)
        self.caixa.adicionar_produto(Mexicabo_carne_geleia)
        self.caixa.adicionar_produto(franbacon)
        self.caixa.adicionar_produto(xtudao)
        self.caixa.adicionar_produto(Big_frango)
        self.caixa.adicionar_produto(Big_Vegetariano)
        self.caixa.adicionar_produto(doce_leite)
        self.caixa.adicionar_produto(prestigio)
        self.caixa.adicionar_produto(nutele)
        self.caixa.adicionar_produto(Romeu_Julieta)
        self.caixa.adicionar_produto(guarana)
        self.caixa.adicionar_produto(fanta)
        self.caixa.adicionar_produto(coca_2l)
        self.caixa.adicionar_produto(coca_zero)
        self.caixa.adicionar_produto(coca_cola_1l)
        self.caixa.adicionar_produto(guarana_2l)
        self.caixa.adicionar_produto(fanta_2l)


    def abrir_relatorio(self):
        self.abrir_login()

    def vender_produto(self):
        print("Vendendo produto...")

    def editar_produto(self):
        if self.abrir_login():
            self.abrir_tela_editar()


    def abrir_login(self):
        self.login_window = LoginWindow()
        if self.login_window.exec_() == QtWidgets.QDialog.Accepted:
            return True
        return False

    def adicionar_produto1(self):
        # Aqui você deve capturar os dados do produto a partir dos campos de entrada da tela de inserção
        nome = self.inserir_window.lineEdit.text()
        preco = float(self.inserir_window.lineEdit_2.text())  # Supondo que tenha um campo para preço
        tipo = self.inserir_window.comboBox.currentText()  # Supondo que tenha um combo box para tipo de produto

        # Crie uma instância do produto com os dados coletados
        if tipo == "PASTEL":
            produto = Pastel(nome, preco)
        elif tipo == "BEBIDA":
            produto = Bebidas(nome, preco)
        elif tipo == "AÇAI":
            produto = Acai(nome, preco)
        elif tipo == "SORVETE":
            produto = Sorvete(nome, preco)
        elif tipo == "CUZCUZ":
            produto = Cuzcuz(nome, preco)
        elif tipo == "MASSA":
            produto = Massa(nome, preco)
        elif tipo == "PETISCO":
            produto = Petisco(nome, preco)
        else:
            print("Tipo de produto inválido.")
            return

        # Chame o método adicionar_produto
        self.caixa.adicionar_produto(produto)

        # Feche a janela de inserção após adicionar
        self.inserir_window.accept()

    def abrir_tela_editar(self):
        self.editar_window = QtWidgets.QDialog()
        uic.loadUi('ui\\editar.ui', self.editar_window)

        # Desconectar sinal se já estiver conectado
        try:
            self.editar_window.lineEdit.textChanged.disconnect(self.buscar_produto)
        except TypeError:
            pass  # Ignorar se não houver conexão

        # Conectar o campo de pesquisa
        self.editar_window.lineEdit.textChanged.connect(self.buscar_produto)
        self.editar_window.tableWidget.itemChanged.connect(self.atualizar_produto)

        # Conectar os botões de inserir e remover
        self.editar_window.pushButton_7.clicked.connect(self.chamar_tela_insercao)
        self.editar_window.pushButton_5.clicked.connect(self.chamar_tela_remocao)

        # Exibir as imagens
        self.exibir_imagem_inserir(self.editar_window)
        self.exibir_imagem_editar(self.editar_window)
        self.exibir_imagem_remover(self.editar_window)
        self.exibir_imagem_pesquisa(self.editar_window)

        # Definir ícone do botão de voltar
        self.definir_imagem_voltar(self.editar_window)

        self.editar_window.exec_()

    def chamar_tela_insercao(self):
        print("Botão Inserir pressionado")  # Debugging
        self.inserir_window = QtWidgets.QDialog()
        uic.loadUi(r'ui\inserir.ui', self.inserir_window)

        # Conectar o botão de adicionar
        self.inserir_window.pushButton.clicked.connect(self.adicionar_produto1)

        self.definir_imagem_voltar(self.inserir_window)
        self.inserir_window.exec_()

    


    def chamar_tela_remocao(self):
        # Abre a tela de remoção
        self.remover_window = QtWidgets.QDialog()
        uic.loadUi('ui\\remover.ui', self.remover_window)  # Carrega a interface de remoção

        self.definir_imagem_remover(self.remover_window)

        # Conectar a pesquisa ao campo de texto
        self.remover_window.lineEdit.textChanged.connect(self.buscar_produto_remocao)
        # Conectar a remoção ao clique no botão de remoção
        self.remover_window.pushButton.clicked.connect(self.remover_produto_selecionado)

        # Conectar as imagens e o botão de voltar
        self.definir_imagem_voltar(self.remover_window)
        self.exibir_imagem_pesquisa(self.remover_window)
        #self.exibir_imagem_lixeira(self.remover_window)


        self.remover_window.exec_()

    def buscar_produto_remocao(self):
        texto_pesquisa = self.remover_window.lineEdit.text().lower()

        # Limpar a tabela para uma nova pesquisa
        self.remover_window.tableWidget.clearContents()
        self.remover_window.tableWidget.setRowCount(0)

        if not texto_pesquisa:
            return

        conn = self.caixa.conectar_bd()
        if not conn:
            QtWidgets.QMessageBox.warning(self.remover_window, "Erro", "Não foi possível conectar ao banco de dados.")
            return

        try:
            with conn.cursor() as cursor:
                query = """
                SELECT id, nome, unidade, preco 
                FROM produtos 
                WHERE LOWER(nome) LIKE %s
                """
                cursor.execute(query, (f"{texto_pesquisa}%",))
                produtos = cursor.fetchall()

                linha = 0
                for produto in produtos:
                    id_produto, nome, unidade, preco = produto

                    self.remover_window.tableWidget.insertRow(linha)

                    # Adicionar os dados visíveis na tabela
                    self.remover_window.tableWidget.setItem(linha, 0, QtWidgets.QTableWidgetItem(nome))  # Nome
                    self.remover_window.tableWidget.setItem(linha, 1, QtWidgets.QTableWidgetItem(unidade))  # Unidade
                    self.remover_window.tableWidget.setItem(linha, 2, QtWidgets.QTableWidgetItem(f"{preco:.2f}"))  # Preço

                    # Associar o ID como dado oculto no item da primeira coluna
                    self.remover_window.tableWidget.item(linha, 0).setData(QtCore.Qt.UserRole, id_produto)
                    linha += 1

            # Ajusta o tamanho das colunas
            self.remover_window.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.remover_window.tableWidget.setColumnWidth(0, 200)  # Nome com largura maior
            self.remover_window.tableWidget.setColumnWidth(1, 100)  # Unidade
            self.remover_window.tableWidget.setColumnWidth(2, 100)  # Preço

        except Exception as e:
            QtWidgets.QMessageBox.critical(self.remover_window, "Erro", f"Erro ao buscar produtos: {e}")
        finally:
            conn.close()



    def remover_produto_selecionado(self):
        # Verificar se alguma linha foi selecionada
        selected_row = self.remover_window.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self.remover_window, "Erro", "Nenhum produto selecionado.")
            return

        # Obter o nome do produto selecionado e o ID oculto
        nome_produto = self.remover_window.tableWidget.item(selected_row, 0).text()
        id_produto = self.remover_window.tableWidget.item(selected_row, 0).data(QtCore.Qt.UserRole)

        # Exibir caixa de diálogo para confirmação da remoção
        reply = QtWidgets.QMessageBox.question(
            self.remover_window, 
            'Confirmar Remoção', 
            f"Tem certeza de que deseja remover o produto '{nome_produto}'?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, 
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            conn = self.caixa.conectar_bd()
            if not conn:
                QtWidgets.QMessageBox.warning(self.remover_window, "Erro", "Não foi possível conectar ao banco de dados.")
                return

            try:
                with conn.cursor() as cursor:
                    query = "DELETE FROM produtos WHERE id = %s"
                    cursor.execute(query, (id_produto,))
                    conn.commit()

                    # Remover a linha da tabela
                    self.remover_window.tableWidget.removeRow(selected_row)

                    QtWidgets.QMessageBox.information(self.remover_window, "Sucesso", "Produto removido com sucesso.")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self.remover_window, "Erro", f"Erro ao remover o produto: {e}")
            finally:
                conn.close()
        else:
            QtWidgets.QMessageBox.information(self.remover_window, "Cancelado", "A remoção foi cancelada.")



    def buscar_produto(self):
        # Captura o texto inserido no campo de pesquisa
        texto_pesquisa = self.editar_window.lineEdit.text().lower()

        # Bloquear sinais para evitar que 'itemChanged' seja chamado durante a atualização
        self.editar_window.tableWidget.blockSignals(True)

        # Limpa o conteúdo atual da tabela
        self.editar_window.tableWidget.clearContents()
        self.editar_window.tableWidget.setRowCount(0)

        # Se o campo de pesquisa estiver vazio, não faz nada e retorna
        if not texto_pesquisa:
            self.editar_window.tableWidget.blockSignals(False)
            return

        # Conectar ao banco de dados
        conn = self.caixa.conectar_bd()
        if not conn:
            print("Erro: não foi possível conectar ao banco de dados.")
            self.editar_window.tableWidget.blockSignals(False)
            return

        try:
            with conn.cursor() as cursor:
                # Consulta SQL para buscar produtos no banco
                query = """
                SELECT id, nome, unidade, preco, tipo 
                FROM produtos 
                WHERE LOWER(nome) LIKE %s
                """
                cursor.execute(query, (f"{texto_pesquisa}%",))
                produtos = cursor.fetchall()

                # Preencher a tabela com os produtos encontrados
                for linha, produto in enumerate(produtos):
                    produto_id, nome, unidade, preco, tipo = produto

                    # Insere uma nova linha na tabela
                    self.editar_window.tableWidget.insertRow(linha)

                    # Criar itens da tabela
                    item_nome = QtWidgets.QTableWidgetItem(nome)
                    item_unidade = QtWidgets.QTableWidgetItem(unidade)
                    item_preco = QtWidgets.QTableWidgetItem(f"{preco:.2f}")

                    # Associar o ID do produto ao item (para referência futura)
                    item_nome.setData(QtCore.Qt.UserRole, produto_id)
                    item_unidade.setData(QtCore.Qt.UserRole, produto_id)
                    item_preco.setData(QtCore.Qt.UserRole, produto_id)

                    # Adicionar itens à tabela
                    self.editar_window.tableWidget.setItem(linha, 0, item_nome)
                    self.editar_window.tableWidget.setItem(linha, 1, item_unidade)
                    self.editar_window.tableWidget.setItem(linha, 2, item_preco)

                # Ajusta o tamanho das colunas
                self.editar_window.tableWidget.horizontalHeader().setStretchLastSection(True)
                self.editar_window.tableWidget.setColumnWidth(0, 200)  # Nome com largura maior
                self.editar_window.tableWidget.setColumnWidth(1, 100)  # Unidade
                self.editar_window.tableWidget.setColumnWidth(2, 100)  # Preço

        except Exception as e:
            print("Erro ao buscar produtos:", e)

        finally:
            conn.close()  # Fecha a conexão ao banco

        # Desbloquear sinais após a atualização
        self.editar_window.tableWidget.blockSignals(False)







    def atualizar_produto(self, item):
        # Bloquear sinais para evitar loops recursivos
        self.editar_window.tableWidget.blockSignals(True)

        # Recuperar o ID do produto associado ao item
        produto_id = item.data(QtCore.Qt.UserRole)

        if produto_id:
            col = item.column()
            nova_info = item.text()

            # Conectar ao banco de dados
            conn = self.caixa.conectar_bd()
            if not conn:
                print("Erro: não foi possível conectar ao banco de dados.")
                self.editar_window.tableWidget.blockSignals(False)
                return

            try:
                with conn.cursor() as cursor:
                    # Atualizar no banco de dados com base na coluna modificada
                    if col == 0:  # Nome
                        query = "UPDATE produtos SET nome = %s WHERE id = %s"
                    elif col == 1:  # Unidade
                        query = "UPDATE produtos SET unidade = %s WHERE id = %s"
                    elif col == 2:  # Preço
                        try:
                            nova_info = float(nova_info)  # Certifique-se de que o preço é válido
                        except ValueError:
                            QtWidgets.QMessageBox.warning(self.editar_window, "Erro", "Por favor, insira um preço válido.")
                            self.editar_window.tableWidget.blockSignals(False)
                            return
                        query = "UPDATE produtos SET preco = %s WHERE id = %s"
                    else:
                        self.editar_window.tableWidget.blockSignals(False)
                        return

                    # Executa a atualização no banco de dados
                    cursor.execute(query, (nova_info, produto_id))
                    conn.commit()

            except Exception as e:
                print("Erro ao atualizar produto:", e)
                QtWidgets.QMessageBox.warning(self.editar_window, "Erro", "Não foi possível atualizar o produto.")

            finally:
                conn.close()  # Fecha a conexão ao banco

        # Reativar o sinal de 'itemChanged' após a atualização
        self.editar_window.tableWidget.blockSignals(False)







    def definir_imagem_voltar(self, window):
        voltar_icon = QtGui.QIcon(r'PROJETOS1\21797173-seta-esquerda-icone-isolado-em-branco-fundo-vetor (1).jpg')  
        window.pushButton_2.setIcon(voltar_icon)
        window.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        window.pushButton_2.clicked.connect(window.reject)

    def definir_imagem_remover(self, window):
        remover_icon = QtGui.QIcon(r'PROJETOS1\trash_5311905.png')  
        window.pushButton.setIcon(remover_icon)
        window.pushButton.setIconSize(QtCore.QSize(110, 110))

    

    def exibir_imagem_inserir(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\check_15526414.png")  # Substitua pelo caminho correto da imagem de inserir
        self.ajustar_imagem(pixmap, window.label_4)  # Ajuste o nome do botão

    def exibir_imagem_editar(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\square_14034491.png")  # Substitua pelo caminho correto da imagem de editar
        self.ajustar_imagem(pixmap, window.label_6)  # Ajuste o nome do botão

    def exibir_imagem_remover(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\square_14034319.png")  # Substitua pelo caminho correto da imagem de remover
        self.ajustar_imagem(pixmap, window.label_8)  # Ajuste o nome do botão

    def exibir_imagem_pesquisa(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\search.png")  # Substitua pelo caminho correto da imagem da pesquisa
        self.ajustar_imagem(pixmap, window.label_10)  # Ajuste o nome do campo da pesquisa
    
    def exibir_imagem_lixeira(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\trash_5311905.png")
        self.ajustar_imagem(pixmap, window.label_10)


    
    def abrir_tela_vender(self):
        self.vender_window = QtWidgets.QDialog()
        uic.loadUi('ui/comandas.ui', self.vender_window)

        # Conectar os botões
        self.vender_window.pushButton_7.clicked.connect(self.abrir_tela_abrir_comanda)

        self.definir_imagem_voltar(self.vender_window)
        self.definir_img_abrir_comanda(self.vender_window)
        self.definir_img_fechar_comanda(self.vender_window)
        self.exibir_img_add_produto(self.vender_window)
        self.exibir_imd_delete_produto(self.vender_window)
        self.exibir_img_abrir_comanda(self.vender_window)
        self.exibir_img_fechar_comanda(self.vender_window)
        self.exibir_img_reabrir_comanda(self.vender_window)

        self.vender_window.exec_()

    def vender_produto(self):
        self.abrir_tela_vender()



    def definir_img_abrir_comanda(self, window):
        add_icon = QtGui.QIcon(r'PROJETOS1\correct_8638664.png')  
        window.pushButton.setIcon(add_icon)
        window.pushButton.setIconSize(QtCore.QSize(50, 50))


    def definir_img_fechar_comanda(self, window):
        cancel_icon = QtGui.QIcon(r'PROJETOS1\cancel_15732086.png')  
        window.pushButton_8.setIcon(cancel_icon)
        window.pushButton_8.setIconSize(QtCore.QSize(87, 87))
    

    def exibir_img_add_produto(self, window):
        add_icon1 = QtGui.QIcon(r'PROJETOS1\add_6217245.png')  
        window.pushButton_3.setIcon(add_icon1)
        window.pushButton_3.setIconSize(QtCore.QSize(40, 40))

    
    def exibir_imd_delete_produto(self, window):
        delete_icon = QtGui.QIcon(r'PROJETOS1\delete_6217704.png')  
        window.pushButton_4.setIcon(delete_icon)
        window.pushButton_4.setIconSize(QtCore.QSize(40, 40))

    def exibir_img_abrir_comanda(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\resize_8637934.png")
        self.ajustar_imagem(pixmap, window.label_4)
    

    def exibir_img_fechar_comanda(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\square_14034319.png")
        self.ajustar_imagem(pixmap, window.label_8)

    
    def exibir_img_reabrir_comanda(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\refresh_9546374.png")
        self.ajustar_imagem(pixmap, window.label_6)
    
    def adicionar_pedidos(self):
        pass

    def adiconar_item_comanda(self):
        pass

    # def exibir_comandas(self):

    #     # Definir o número de colunas (Cliente e Produtos)
    #     self.vender_window.comandas_widget.setColumnCount(2)

    #     # Definir os títulos das colunas
    #     self.vender_window.comandas_widget.setHorizontalHeaderLabels(['Cliente', 'Produtos'])

    #     # Limpar todas as linhas antes de adicionar novas
    #     self.vender_window.comandas_widget.setRowCount(0)

    #     # Filtrar pedidos abertos
    #     lista_pedidos_abertos = [pedido for pedido in self.caixa._pedidos_abertos if pedido._status == "ABERTO"]

    #     row = 0  # Contador de linhas
    #     for pedido in lista_pedidos_abertos:
    #         self.vender_window.comandas_widget.insertRow(row)

    #         # Nome do cliente
    #         item_nome = QtWidgets.QTableWidgetItem(pedido._cliente)
    #         self.vender_window.comandas_widget.setItem(row, 0, item_nome)

    #         # Produtos do pedido
    #         produtos = ", ".join([produto.nome for produto in pedido._produtos])  # Obter os nomes dos produtos
    #         item_produto = QtWidgets.QTableWidgetItem(produtos)
    #         self.vender_window.comandas_widget.setItem(row, 1, item_produto)

    #         row += 1

    def buscar_produto_add_comanda(self):
        texto_pesquisa = self.abrir_window.lineEdit_2.text().lower()

        # Limpar a tabela para uma nova pesquisa
        self.abrir_window.tableWidget.clearContents()
        self.abrir_window.tableWidget.setRowCount(0)

        if not texto_pesquisa:
            return

        # Variável para controlar o número de linhas e rastrear produtos já exibidos
        linha = 0
        produtos_exibidos = set()  # Usar um conjunto para rastrear produtos exibidos

        # Preenche a tabela com os produtos que correspondem ao texto de pesquisa
        for tipo, conteudo in self.caixa._produtos.items():
            if isinstance(conteudo, list):
                for produto in conteudo:
                    if produto._nome.lower().startswith(texto_pesquisa):
                        # Verifica se o nome do produto já foi exibido
                        if produto._nome not in produtos_exibidos:
                            self.abrir_window.tableWidget.insertRow(linha)
                            self.abrir_window.tableWidget.setItem(linha, 0, QtWidgets.QTableWidgetItem(produto._nome))
                            self.abrir_window.tableWidget.setItem(linha, 1, QtWidgets.QTableWidgetItem(produto._unidade))
                            self.abrir_window.tableWidget.setItem(linha, 2, QtWidgets.QTableWidgetItem(f"{produto._preco:.2f}"))
                            
                            produtos_exibidos.add(produto._nome)  # Adiciona o nome do produto ao conjunto
                            linha += 1

        # Ajusta o tamanho das colunas
        self.abrir_window.tableWidget.horizontalHeader().setStretchLastSection(True)

        # Define as proporções das colunas
        self.abrir_window.tableWidget.setColumnWidth(0, 200)  # Nome com largura maior
        self.abrir_window.tableWidget.setColumnWidth(1, 100)  # Unidade
        self.abrir_window.tableWidget.setColumnWidth(2, 100)  # Preço

    def abrir_tela_abrir_comanda(self):
        self.abrir_window = QtWidgets.QDialog()
        uic.loadUi('ui\\abrir_comanda.ui', self.abrir_window)

        # Lista para armazenar os pedidos temporários
        self.pedidos = []

        # Conectar o campo de pesquisa
        self.abrir_window.lineEdit_2.textChanged.connect(self.buscar_produto_add_comanda)

        # Conectar a seleção do ComboBox (tipo de produto)
        self.abrir_window.comboBox.currentIndexChanged.connect(self.selecionar_tipo_venda)

        # Conectar a seleção de linha da tabela
        self.abrir_window.tableWidget.itemSelectionChanged.connect(self.selecionar_produto)

        # Conectar o botão de adicionar ao pedido
        self.abrir_window.pushButton_3.clicked.connect(self.adicionar_produto_pedido)

        # Conectar o botão de confirmar pedido
        self.abrir_window.pushButton.clicked.connect(self.confirmar_pedido)

        # Conectar o botão de cancelar pedido
        self.abrir_window.pushButton_5.clicked.connect(self.cancelar_pedido)

        self.definir_imagem_voltar(self.abrir_window)
        self.exibir_img_add_produto(self.abrir_window)
        self.exibir_imd_delete_produto(self.abrir_window)

        self.abrir_window.exec_()

    def selecionar_tipo_venda(self):
        """Escolhe qual lógica de venda será utilizada com base no ComboBox"""
        tipo_selecionado = self.abrir_window.comboBox.currentText().lower()

        if tipo_selecionado in ["pastel", "bebida"]:
            # Se o tipo selecionado for "Pastel" ou "Bebida", utiliza a lógica de venda com tabela de produtos
            self.abrir_window.lineEdit_2.setEnabled(True)  # Ativa o campo de pesquisa
            self.buscar_produto_add_comanda()  # Exibe a tabela de produtos
        else:
            # Se for outro tipo de venda, desativa a tabela e usa outra lógica
            self.abrir_window.lineEdit_2.setEnabled(False)
            self.abrir_window.tableWidget.clearContents()
            self.abrir_window.tableWidget.setRowCount(0)
            self.outra_logica_venda(tipo_selecionado)

    def buscar_produto_add_comanda(self):
        """Lógica de venda para produtos como pastel e bebida."""
        texto_pesquisa = self.abrir_window.lineEdit_2.text().lower()

        # Limpar a tabela para uma nova pesquisa
        self.abrir_window.tableWidget.clearContents()
        self.abrir_window.tableWidget.setRowCount(0)

        if not texto_pesquisa:
            return

        # Variável para controlar o número de linhas e rastrear produtos já exibidos
        linha = 0
        produtos_exibidos = set()

        # Preenche a tabela com os produtos que correspondem ao texto de pesquisa
        for tipo, conteudo in self.caixa._produtos.items():
            if isinstance(conteudo, list):
                for produto in conteudo:
                    if produto._nome.lower().startswith(texto_pesquisa):
                        # Verifica se o nome do produto já foi exibido
                        if produto._nome not in produtos_exibidos:
                            self.abrir_window.tableWidget.insertRow(linha)
                            self.abrir_window.tableWidget.setItem(linha, 0, QtWidgets.QTableWidgetItem(produto._nome))
                            self.abrir_window.tableWidget.setItem(linha, 1, QtWidgets.QTableWidgetItem(produto._unidade))
                            self.abrir_window.tableWidget.setItem(linha, 2, QtWidgets.QTableWidgetItem(f"{produto._preco:.2f}"))

                            produtos_exibidos.add(produto._nome)
                            linha += 1

        # Ajusta o tamanho das colunas
        self.abrir_window.tableWidget.horizontalHeader().setStretchLastSection(True)

        # Define as proporções das colunas
        self.abrir_window.tableWidget.setColumnWidth(0, 200)  # Nome com largura maior
        self.abrir_window.tableWidget.setColumnWidth(1, 100)  # Unidade
        self.abrir_window.tableWidget.setColumnWidth(2, 100)  # Preço

    def outra_logica_venda(self, tipo_selecionado):
        """Lógica alternativa para outros tipos de venda."""
        QtWidgets.QMessageBox.information(self.abrir_window, "Outra Lógica", f"Lógica de venda para o tipo {tipo_selecionado} ainda será implementada.")

    def selecionar_produto(self):
        # Capturar a linha selecionada
        linha_selecionada = self.abrir_window.tableWidget.currentRow()
        self.produto_selecionado = {
            "nome": self.abrir_window.tableWidget.item(linha_selecionada, 0).text(),
            "unidade": self.abrir_window.tableWidget.item(linha_selecionada, 1).text(),
            "preco": float(self.abrir_window.tableWidget.item(linha_selecionada, 2).text())
        }

    def adicionar_produto_pedido(self):
        quantidade = self.abrir_window.spinBox.value()

        if hasattr(self, 'produto_selecionado') and quantidade > 0:
            # Adiciona o produto selecionado ao pedido
            self.pedidos.append({
                "produto": self.produto_selecionado,
                "quantidade": quantidade
            })

            # Feedback visual ou mensagem
            QtWidgets.QMessageBox.information(self.abrir_window, "Adicionado", f"{quantidade}x {self.produto_selecionado['nome']} adicionado ao pedido.")

        else:
            QtWidgets.QMessageBox.warning(self.abrir_window, "Erro", "Selecione um produto e uma quantidade válida.")

    def confirmar_pedido(self):
        if self.pedidos:
            # Processar o pedido (por exemplo, enviar para o banco de dados ou exibir na tela de confirmação)
            print("Pedido confirmado:", self.pedidos)
            QtWidgets.QMessageBox.information(self.abrir_window, "Pedido", "Pedido confirmado com sucesso!")

            # Fechar a janela após confirmação
            self.abrir_window.accept()

        else:
            QtWidgets.QMessageBox.warning(self.abrir_window, "Erro", "Nenhum produto foi adicionado ao pedido.")

    def cancelar_pedido(self):
        # Limpar o pedido temporário
        self.pedidos = []
        QtWidgets.QMessageBox.information(self.abrir_window, "Cancelado", "O pedido foi cancelado.")
        self.abrir_window.reject()



    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
