from datetime import date
import re
import os
import sqlite3
import datetime
import textwrap
import unicodedata

def menu_interativo1(type):
    x=1
    y=1
    while x==1:
        n=0
        os.system("cls")
        
        cursor.execute('''
                SELECT * FROM produtos WHERE tipo = ?
            ''', (type))
        produtos = cursor.fetchall()
        print('ahdasdhksa')
        for produto in produtos:
            print("{} {}\t\tR$ {}".format (str(produto[1]).center(10),n+1, str(produto[2]).ljust(10)))
            n=n+1
        resposta_cadastro_itens=str(input("Deseja fazer alguma alteração nos produtos que estão a venda ?\n 1 - sim\n 2- nao\nR= "))
        if resposta_cadastro_itens.lower() == "1":
            os.system("cls")
            while y==1:
                resposta_interação=str(input("deseja fazer que tipo de alteração?\n[1] - adicionar itens\n[2]- remover alguns itens\n[3]- refazer toda a lista\n[0]- voltar ao menu principal\nR="))
                if resposta_interação == "1":
                    os.system("cls")
                    adicionar_itens=str(input("Qual item você deseja adicionar ? "))
                    valor_adicionar=float(input("Qual o valor do produto que você deseja adicionar ?\nR$"))
                    a.append(adicionar_itens)
                    b.append(valor_adicionar)
                elif resposta_interação == "2":
                    os.system("cls")
                    n=0
                    for i in range(len (a)):
                        print("{} {}\t\tR$ {}".format(n+1, str(a[i]).center(10), str(b[i]).ljust(10)))
                        n+=1
                    remover_itens=int(input("Por favor, informe qual item você deseja remover: "))
                    del a[remover_itens - 1] 
                    del b[remover_itens - 1]
                elif resposta_interação == "3":
                    l=1
                    os.system("cls")
                    del a[:]
                    del b[:]
                    while l==1:
                        n=0
                        for i in range(len (a)):
                            print("{} {}\t\tR$ {}".format(n+1 ,str(a[i]).center(10), str(b[i]).ljust(10)))
                            n+=1
                        adicionar_itens=str(input("Qual item você deseja adicionar ? "))
                        if adicionar_itens == "":
                            l=0
                        else:
                            valor_adicionar=float(input("Qual o valor do produto que você deseja adicionar ?\nR$"))
                            a.append(adicionar_itens)
                            b.append(valor_adicionar)
                if resposta_interação.lower() == '0':
                    y=0
        if resposta_cadastro_itens.lower() == "2":
            x=0

#função de menu principal do cliente
def menu_principal_cliente(cliente):
    p=1
    while p==1 :
        resposta_principal=int(input("""  

        Escolha os tipos de produtos que você deseja ver e nossa loja 
        1 - Produtos roupas
        2 - Produtos escolares
        3 - Produtos comidas
        0 - encerrar atendimento
        Digite o número correspondente ao tipo produto que deseja: """))
        while True:
            #funçao roupas
            if resposta_principal == 1:
                os.system("cls")
                print("Escolha o tipo de roupa que deseja adquirir")
                
                cursor.execute('''
                SELECT * FROM produto WHERE tipo = 1 AND status = 1
                ''')
                produtos = cursor.fetchall()
                for i, produto in enumerate(produtos):
                    print("({}) {}\t\tR$ {}".format(i+1, produto[1].ljust(10), str(produto[2]).ljust(10)))                    

                print("[0] Voltar para o menu principal")
                print("-" * 50)
                print("carrinho de compras", lista_pedido, sep=" ")
                print("total: R$", sum(lista_valores))
                #funções roupa
                
                resposta_roupa = int(input(" Por Favor, insira o numero do produto que você deseja !!!!\nProduto:"))
                
                if(resposta_roupa == 0):
                    break
                
                lista_pedido.append(produtos[resposta_roupa - 1][1])
                lista_valores.append(produtos[resposta_roupa - 1][2])

            #funções escolares 
            elif resposta_principal == 2:
                os.system("cls")
                print("Escolha o tipo de escolares que deseja adquirir")

                cursor.execute('''
                SELECT * FROM produto WHERE tipo = 2 AND status = 1
                ''')
                produtos = cursor.fetchall()
                for i, produto in enumerate(produtos):
                    print("({}) {}\t\tR$ {}".format(i+1, produto[1].ljust(10), str(produto[2]).ljust(10)))
                    
                print("[0] Voltar para o menu principal")
                print("-" * 50)
                print(lista_pedido)
                print("total: R$", sum(lista_valores))
                
                resposta_escolares = int(input(" Por Favor, insira o numero do produto que você deseja !!!!\nProduto:"))
                
                if(resposta_escolares == 0):
                    break
                
                lista_pedido.append(produtos[resposta_escolares - 1][1])
                lista_valores.append(produtos[resposta_escolares - 1][2])
            
            #funções comidas 
            elif resposta_principal == 3:
                os.system("cls")
                print("Escolha o tipo de produtos que deseja adquirir")

                cursor.execute('''
                SELECT * FROM produto WHERE tipo = 3 AND status = 1
                ''')
                produtos = cursor.fetchall()
                for i, produto in enumerate(produtos):
                    print("({}) {}\t\tR$ {}".format(i+1, produto[1].ljust(10), str(produto[2]).ljust(10))) 
                    
                print("[0] Voltar para o menu principal")
                print("-" * 50)
                print(lista_pedido)
                print("total: R$", sum(lista_valores))
                
                resposta_comidas = int(input(" Por Favor, insira o numero do produto que você deseja !!!!\nProduto:"))
                
                if(resposta_comidas == 0):
                    break
                
                lista_pedido.append(produtos[resposta_comidas - 1][1])
                lista_valores.append(produtos[resposta_comidas - 1][2])    
                
            elif resposta_principal > 3 or resposta_principal < 0 :
                print("opção invalida")
            #encerrar o programa e emitir a nota fiscal
            elif resposta_principal == 0:
                pedido_id = criar_pedido(cliente[0], sum(lista_valores))
                for produto in lista_pedido:
                    criar_pedido_produtos(pedido_id, produto)
                
                #os.system("cls")
                nota_fiscal = textwrap.dedent('''
                    Obrigado por utilizar nossos produtos e nossa loja !!!
                    Aqui está sua nota fiscal !\n\n\n\n
                    * NOTA FISCAL *
                    {}
                    nome: {}
                    Endereço: {} {} {}
                    CPF/CNPJ: {}
                    Cidade: Curitiba
                    UF: PR
                    CEP: {}
                    -----------------------------
                    PRODUTO\t\t\tPREÇO
                    '''.format(data_hoje, str(cliente[1]), str(cliente[3]), str(cliente[5]), str(cliente[4]), str(cliente[6]), str(cliente[2])))

                for i in range(len(lista_pedido)):
                    produto_formatado = "{}\t\tR$ {:.2f}".format(lista_pedido[i].ljust(8), lista_valores[i])
                    nota_fiscal += produto_formatado + '\n'

                nota_fiscal += textwrap.dedent('''
                    -----------------------------
                    TOTAL:\t\tR$ {:.2f}
                    '''.format(sum(lista_valores)))
                print(nota_fiscal)
                exit()

# função de menu principal do lojista
def menu_principal_loja():
    o=1
    b=0
    c=1
    while o==1:
        os.system("cls")
        resposta_menu_loja=int(input(f"Olá seja bem vindo ao gerenciamento de estoque\no que você precisa para hoje ?\n[1] - Ver estoque dos produtos\n[2] - entrar no menu de compras\n[0] -  voltar ao menu de login\nR="))
        while True:
            if resposta_menu_loja == 0:
                inicio()

            elif resposta_menu_loja == 1:
                while c==1:
                    os.system("cls")
                    resposta_menu_produtos=int(input("Quais tipos de produtos você quer conferir ?\n[1]- Produtos roupas\n[2]- Produtos escolares\n[3]-  Produtos Comidas\n[0] voltar\nR="))
                    if resposta_menu_produtos == 1:
                        menu_interativo1(TIPO_ROUPA)
                    elif resposta_menu_produtos == 2:
                        menu_interativo1(TIPO_ESCOLA)
                    elif resposta_menu_produtos == 3:
                        menu_interativo1(TIPO_COMIDA)
                    elif resposta_menu_produtos > 3 or resposta_menu_produtos < 0:
                        print("opção invalida")
                    elif resposta_menu_produtos == 0:
                        c=0
                    elif  resposta_menu_produtos > 5 or resposta_menu_produtos< 0:
                        print("opção invalida")
            elif resposta_menu_loja == 2:
                menu_principal_cliente(b)
            elif resposta_menu_loja > 3 or resposta_menu_loja < 0 :
                break

#Verificações 

def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if not unicodedata.combining(c))

#Verificar CPF
def verificar_cpf(cpf):
    #Remover pontuação do CPF
    cpf = cpf.replace(".","").replace("-","")

    #Verificar se o cpf possui 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    #Verificar se todos os dígitos são iguais , o que indica um CPF inválido
    if cpf == cpf[0] * 11:
        return False
    
    #Verificar o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range (9))
    digito_1 = (soma * 10) % 11
    if digito_1 == 10:
        digito_1 = 0

    if digito_1 != int(cpf[9]):
        return False
    

    #Verifica o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_2 = (soma * 10) % 11 
    if digito_2 == 10:
        digito_2 = 0

    if digito_2 != int(cpf[10]):
        return False
    
    return True

# Função para verificar se uma string contém apenas letras
def verificar_letras(string):
    if not string.replace(" ", "").isalpha():
        return False
    return True

# Função para verificar se uma string contém apenas números
def verificar_numeros(string):
    if not string.isdigit():
        return False
    return True

# Expressão regular para verificar o formato do email
def verificar_email(email):
    
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao_email, email):
        return True
    else:
        return False

# Expressão regular para verificar o formato do CEP
def verificar_cep(cep):
    
    padrao_cep = r'^\d{5}-?\d{3}$'
    if re.match(padrao_cep, cep):
        return True
    else:
        return False
    
def criar_pedido(cliente_id, valor_pedido):
    cursor.execute('''
        INSERT INTO pedido (cliente_id, valor)
        VALUES (?, ?)
    ''', (cliente_id, valor_pedido))
    conexao.commit()
    
    cursor.execute("SELECT * FROM pedido ORDER BY rowid DESC LIMIT 1")
    return cursor.fetchone()[0]
    
def criar_pedido_produtos(pedido_id, produto):
    cursor.execute('''
        SELECT * FROM produto WHERE nome = ?
    ''', (produto,))
    produto_id = cursor.fetchone()[0]

    cursor.execute('''
        INSERT INTO pedido_produtos (pedido_id, produto_id)
            VALUES (?, ?)
    ''', (pedido_id, produto_id))
    conexao.commit()


# Obter data de hoje
data_hoje = date.today()

#cadastros de cliente
email_cliente_db=["teste1"]
senha_cliente_db=["teste1"]
#cadastros de lojista
email_loja_db=["teste2"]
senha_loja_db=["teste2"]
#lista de produtos para calculos

valores_roupas=[150.00,100.00,180.00,120.00,60.00,300.00,190.00]
valores_escolares=[2.00,139.90,3.00,20.00]
valores_comidas=[7.00,4.00,5.00,6.00,8.00]
vr=valores_roupas
ve=valores_escolares
vc=valores_comidas

#lista cadastro cliente
cadastro_cliente=[]
cadastro_cpfcnpj=[]
cadastro_endereco=[]
cadastro_complemento=[]
cadastro_numero_casa=[]
cadastro_cep=[]

#lista de produtos para o menu 
produtos_roupas=[
    "Tenis","Camisa","Jaqueta","Calça","Boné","Relogio","Perfume",
]
produtos_escolares=[
    "lápis","Mochila","Caneta","Agenda",]
produtos_comidas=[
    "C/Estudante","Café","Refri","Salgados","Suco"
]

TIPO_ROUPA = 1
TIPO_ESCOLA = 2
TIPO_COMIDA = 3

lista_produtos = []
lista_produtos.extend([(prod, valor, TIPO_ROUPA) for prod, valor in zip(produtos_roupas, valores_roupas)])
lista_produtos.extend([(prod, valor, TIPO_ESCOLA) for prod, valor in zip(produtos_escolares, valores_escolares)])
lista_produtos.extend([(prod, valor, TIPO_COMIDA) for prod, valor in zip(produtos_comidas, valores_comidas)])

pr=produtos_roupas
pe=produtos_escolares
pc=produtos_comidas
#Carrinho de compras e o valor total gerado 
lista_pedido=[]
lista_valores=[]

# Conectar ao banco de dados
conexao = sqlite3.connect('cadastro.db')
cursor = conexao.cursor()

# Criação das tabelas se não existirem
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf_cnpj TEXT,
        endereco TEXT,
        complemento TEXT,
        numero_casa TEXT,
        cep TEXT,
        email TEXT,
        senha TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS lojista (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf_cnpj TEXT,
        endereco TEXT,
        complemento TEXT,
        numero_casa TEXT,
        cep TEXT,
        email TEXT,
        senha TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco REAL,
        tipo INTEGER,
        status BOOLEAN
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedido (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        valor REAL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedido_produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pedido_id INTEGER,
        produto_id INTEGER,
        quantidade INTEGER
    )
''')

cursor.execute('SELECT * FROM produto')
row = cursor.fetchone()
if not row:
    for index, produto in enumerate(lista_produtos):
        cursor.execute('''
        INSERT INTO produto (id, nome, preco, tipo, status)
            VALUES (?, ?, ?, ?, ?)
        ''', (index, produto[0], produto[1], produto[2], 1))
        conexao.commit()

def inicio():

    print('''
Bem-vindo à nossa loja!

Nós estamos muito felizes em recebê-lo em nosso estabelecimento. Aqui você encontrará uma variedade de produtos de alta qualidade para atender às suas necessidades.

Agradecemos por escolher a nossa loja e esperamos que você tenha uma experiência agradável e satisfatória. Seja bem-vindo!

Atenciosamente,
Equipe da loja
'''
)
    # Perguntar se é um cliente ou lojista
    resposta_inicio = input('''Você é um Cliente ou Lojista? (Responda "Cliente" ou "Lojista")\nR: ''')

    while not resposta_inicio or resposta_inicio.lower() not in ["cliente", "lojista"]:
        if not resposta_inicio:
            print("Resposta vazia. Por favor, responda novamente.")
        else:
            print("Resposta inválida. Por favor, responda com 'Cliente' ou 'Lojista'.")
        resposta_inicio = input('''Você é um cliente ou lojista? (Responda "Cliente" ou "Lojista")\nR: ''')

    if resposta_inicio.lower() == "cliente":
        # Cadastro de cliente
        resposta_cliente = input('''Você já possui o cadastro de cliente? ("Sim" ou "Não")\nR: ''')
        while not resposta_cliente or remover_acentos(resposta_cliente.lower()) not in ["sim", "nao"]:
            if not resposta_cliente:
                print("Resposta vazia. Por favor, responda novamente.")
            else:
                print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")
            resposta_cliente = input('Você já possui o cadastro de lojista? ("Sim" ou "Não")\nR: ')
            
        resposta_cliente = remover_acentos(resposta_cliente.lower())

        if resposta_cliente.lower() == "nao":
            print("Vamos começar o seu cadastro então:")
            # Informações registro do cliente
            cliente_teste = input("Primeiro, por favor insira o seu nome: ")
            while not cliente_teste or not verificar_letras(cliente_teste):
                if not cliente_teste:
                    print("Resposta vazia. Por favor, insira o seu nome.")
                else:
                    print("Nome inválido. Por favor, insira um nome válido.")
                cliente_teste = input("Primeiro, por favor insira o seu nome: ")

            cpf_cnpj = input("Em seguida, o seu CPF (Se desejar): ")
            while cpf_cnpj and not verificar_cpf(cpf_cnpj):
                print("CPF inválido. Por favor, insira um CPF válido.")
                cpf_cnpj = input("Em seguida, o seu CPF (Se desejar): ")

            # Verificar se o CPF já está cadastrado
            cursor.execute('''
                SELECT * FROM cliente WHERE cpf_cnpj = ?
            ''', (cpf_cnpj,))
            cliente_existente = cursor.fetchone()

            while cliente_existente:
                print("CPF já cadastrado. Por favor, insira um CPF diferente.")
                cpf_cnpj = input("Em seguida, o seu CPF (Se desejar): ")
                while cpf_cnpj and not verificar_cpf(cpf_cnpj):
                    if not cpf_cnpj:
                        print("Resposta vazia. Por favor, insira o seu CPF.")
                    else:
                        print("CPF inválido. Por favor, insira um CPF válido.")
                    cpf_cnpj = input("Em seguida, o seu CPF (Se desejar): ")

                cursor.execute('''
                    SELECT * FROM cliente WHERE cpf_cnpj = ?
                ''', (cpf_cnpj,))
                cliente_existente = cursor.fetchone()

            endereco_teste = input("Por favor, insira o seu endereço (Sem o número): ")
            while not endereco_teste or not verificar_letras(endereco_teste):
                if not endereco_teste:
                    print("Resposta vazia. Por favor, insira o seu endereço. ")
                else:
                    print("Endereço inválido. Por favor, insira um endereço válido. ")
                endereco_teste = input("Por favor, insira o seu endereço (Sem o número): ")


            complemento_casa = input("Digite um complemento: ")
            while not complemento_casa or not verificar_letras(complemento_casa):
                if not complemento_casa:
                    print("Resposta vazia. Por favor, insira um complemento.")
                else:
                    print("Complemento inválido. Por favor, insira um complemento válido.")
                complemento_casa = input("Digite um complemento para sua casa: ")

            numero_casa = input("Agora insira o número da casa: ")
            while not numero_casa or not verificar_numeros(numero_casa):
                if not numero_casa:
                    print("Resposta vazia. Por favor, insira o número da casa.")
                else:
                    print("Número inválido. Por favor, insira um número válido.")
                numero_casa = input("Agora insira o número da casa: ")

            cep_teste = input("Insira o CEP (Somente números): ")
            while not cep_teste or (cep_teste and not verificar_cep(cep_teste)):
                if not cep_teste:
                    print("Resposta vazia. Por favor, insira o CEP.")
                else:
                    print("CEP inválido. Por favor, insira um CEP válido.")
                cep_teste = input("Insira o CEP (Somente números): ")

            registro_cliente_email = input("Digite o seu email: ")
            while not registro_cliente_email or not verificar_email(registro_cliente_email):
                if not registro_cliente_email:
                    print("Resposta vazia. Por favor, insira o seu email.")
                else:
                    print("Email inválido. Por favor, insira um email válido.")
                registro_cliente_email = input("Digite o seu email: ")

            # Verificar se o email já está cadastrado
            cursor.execute('''
                SELECT * FROM cliente WHERE email = ?
            ''', (registro_cliente_email,))
            email_existente = cursor.fetchone()

            while email_existente:
                print("Email já cadastrado. Por favor, insira um email diferente.")
                registro_cliente_email = input("Digite o seu email: ")
                while not registro_cliente_email or not verificar_email(registro_cliente_email):
                    if not registro_cliente_email:
                        print("Resposta vazia. Por favor, insira o seu email.")
                    else:
                        print("Email inválido. Por favor, insira um email válido.")
                    registro_cliente_email = input("Digite o seu email: ")

                cursor.execute('''
                    SELECT * FROM cliente WHERE email = ?
                ''', (registro_cliente_email,))
                email_existente = cursor.fetchone()

            registro_cliente_senha = input("Digite uma senha: ")
            
            # Correção do CPF Nulo
            if not cpf_cnpj:
                cpf_cnpj = None

            # Inserir os dados do cliente no banco de dados
            cursor.execute('''
                INSERT INTO cliente (nome, cpf_cnpj, endereco, complemento, numero_casa, cep, email, senha)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (cliente_teste, cpf_cnpj, endereco_teste, complemento_casa, numero_casa, cep_teste, registro_cliente_email, registro_cliente_senha))

            conexao.commit()
            print("Cadastro realizado com sucesso!")
            inicio()

        elif resposta_cliente.lower() == "sim":
            login_sucesso = False

            while not login_sucesso:
                email_cliente = input("Digite seu email: ")
                senha_cliente = input("Digite sua senha: ")

                # Verificar se o email existe no banco de dados
                cursor.execute('''
                    SELECT * FROM cliente WHERE email = ?
                ''', (email_cliente,))

                cliente = cursor.fetchone()

                if cliente is not None:
                    # Verificar se a senha corresponde ao email encontrado
                    if senha_cliente == cliente[8]:
                        login_sucesso = True
                        print("Login realizado com sucesso!")
                        print("Bem-vindo, {}!".format(cliente[1]))
                        menu_principal_cliente(cliente)
                    else:
                        print("Senha incorreta. Tente novamente.")
                else:
                    print("Email não cadastrado. Tente novamente.")


    elif resposta_inicio.lower() == "lojista":
        # Cadastro de lojista
        resposta_lojista = input('Você já possui o cadastro de lojista? ("Sim" ou "Não")\nR: ')

        while not resposta_lojista or remover_acentos(resposta_lojista.lower()) not in ["sim", "nao"]:
            if not resposta_lojista:
                print("Resposta vazia. Por favor, responda novamente.")
            else:
                print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")
            resposta_lojista = input('Você já possui o cadastro de lojista? ("Sim" ou "Não")\nR: ')

        resposta_lojista = remover_acentos(resposta_lojista.lower())


        if resposta_lojista.lower() == "nao":
                print("Vamos começar o seu cadastro então:")
                # Informações de registro do lojista
                lojista_teste = input("Primeiro, por favor insira o seu nome: ")
                while not lojista_teste or not verificar_letras(lojista_teste):
                    if not lojista_teste:
                        print("Resposta vazia. Por favor, insira o seu nome.")
                    else:
                        print("Nome inválido. Por favor, insira um nome válido.")
                    lojista_teste = input("Primeiro, por favor insira o seu nome: ")

                cpf_cnpj = input("Em seguida, insira o seu CPF: ")
                while cpf_cnpj and not verificar_cpf(cpf_cnpj):
                    if not cpf_cnpj:
                        print("Resposta vazia. Por favor, insira o seu CPF.")
                    else:
                        print("CPF inválido. Por favor, insira um CPF válido.")
                    cpf_cnpj = input("Em seguida, insira o seu CPF: ")

                # Verificar se o CPF já está cadastrado
                cursor.execute('SELECT * FROM lojista WHERE cpf_cnpj = ?', (cpf_cnpj,))
                lojista_existente = cursor.fetchone()

                while lojista_existente:
                    print("CPF já cadastrado. Por favor, insira um CPF diferente.")
                    cpf_cnpj = input("Em seguida, insira o seu CPF: ")
                    while cpf_cnpj and not verificar_cpf(cpf_cnpj):
                        print("CPF inválido. Por favor, insira um CPF válido.")
                        cpf_cnpj = input("Em seguida, insira o seu CPF: ")
                    cursor.execute('SELECT * FROM lojista WHERE cpf_cnpj = ?', (cpf_cnpj,))
                    lojista_existente = cursor.fetchone()

                endereco_teste = input("Por favor, insira o seu endereço (Sem o número): ")
                while not endereco_teste or not verificar_letras(endereco_teste):
                    if not endereco_teste:
                        print("Resposta vazia. Por favor, insira o seu endereço. ")
                    else:
                        print("Endereço inválido. Por favor, insira um endereço válido. ")
                    endereco_teste = input("Por favor, insira o seu endereço (Sem o número): ")

                complemento_casa = input("Digite um complemento: ")
                while not complemento_casa or not verificar_letras(complemento_casa):
                    if not complemento_casa:
                        print("Resposta vazia. Por favor, insira um complemento.")
                    else:
                        print("Complemento inválido. Por favor, insira um complemento válido.")
                    complemento_casa = input("Digite um complemento para sua casa: ")

                numero_casa = input("Agora insira o número da casa: ")
                while not numero_casa or not verificar_numeros(numero_casa):
                    if not numero_casa:
                        print("Resposta vazia. Por favor, insira o número da casa.")
                    else:
                        print("Número inválido. Por favor, insira um número válido.")
                    numero_casa = input("Agora insira o número da casa: ")

                cep_teste = input("Insira o CEP (Somente números): ")
                while not cep_teste or (cep_teste and not verificar_cep(cep_teste)):
                    if not cep_teste:
                        print("Resposta vazia. Por favor, insira o CEP.")
                    else:
                        print("CEP inválido. Por favor, insira um CEP válido.")
                    cep_teste = input("Insira o CEP (Somente números): ")

                registro_lojista_email = input("Digite o seu email: ")
                while not registro_lojista_email or not verificar_email(registro_lojista_email):
                    print("Email inválido. Por favor, insira um email válido.")
                    registro_lojista_email = input("Digite o seu email: ")

                # Verificar se o email já está cadastrado
                cursor.execute('''
                    SELECT * FROM lojista WHERE email = ?
                ''', (registro_lojista_email,))
                email_existente = cursor.fetchone()

                while email_existente:
                    print("Email já cadastrado. Por favor, insira um email diferente.")
                    registro_lojista_email = input("Digite o seu email: ")
                    while not verificar_email(registro_lojista_email):
                        print("Email inválido")
                        registro_lojista_email = input("Digite o seu email: ")

                    cursor.execute('''
                        SELECT * FROM lojista WHERE email = ?
                    ''', (registro_lojista_email,))
                    email_existente = cursor.fetchone()

                registro_lojista_senha = input("Digite uma senha: ")

                # Inserir os dados do lojista no banco de dados
                cursor.execute('''
                    INSERT INTO lojista (nome, cpf_cnpj, endereco, complemento, numero_casa, cep, email, senha)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (lojista_teste, cpf_cnpj, endereco_teste, complemento_casa, numero_casa, cep_teste, registro_lojista_email, registro_lojista_senha))

                conexao.commit()
                print("Cadastro realizado com sucesso!")
                menu_principal_loja() 

        elif resposta_lojista.lower() == "sim":
            login_sucesso = False

        while not login_sucesso:
            email_lojista = input("Digite seu email: ")
            senha_lojista = input("Digite sua senha: ")

            # Verificar se o email existe no banco de dados
            cursor.execute('''
                SELECT * FROM lojista WHERE email = ?
            ''', (email_lojista,))

            lojista = cursor.fetchone()

            if lojista is not None:
                # Verificar se a senha corresponde ao email encontrado
                if senha_lojista == lojista[8]:
                    login_sucesso = True
                    print("Login realizado com sucesso!")
                    print("Bem-vindo, {}!".format(lojista[1]))
                    print()  # Linha em branco
                    menu_principal_loja()
                else:
                    print("Senha incorreta. Tente novamente.")
            else:
                print("Email não cadastrado. Tente novamente.")

    conexao.close()

inicio()