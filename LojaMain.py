from datetime import date
import re
import os
import sqlite3
import datetime
# a fazer ainda !!!!!!!!!!! cadastro de itens, terminar menu de lojista

def return_login():
    #login no sistema   
    k=1   
    os.system("cls")
    while k==1:
        print("Por favor insira o seu login")
        email_login=str(input("Email:"))
        senha_login=str(input("Senha:"))
        if email_login in email_cliente_db and senha_login in senha_cliente_db: 
            menu_principal_cliente()
            k=0
        elif email_login in email_loja_db and senha_login in senha_loja_db:
            resposta_login_loja=str(input("Você tem cadastro como lojista \nQual menu você deseja ver ?\n[1] Menu cliente\n[2] Menu lojista \nR= "))
            if resposta_login_loja == "1":
                menu_principal_cliente()
                k=0
            elif resposta_login_loja ==  "2":
                menu_principal_loja()
                k=0
            else:
                print("Desculpa, nao consegui entender o seu pedido")
        else:
            print("Login e/ou senha inválidos, tente novamente")

def menu_interativo1(a,b):
    x=1
    y=1
    while x==1:
        n=0
        os.system("cls")
        for i in range(len(a)):
            print("{} {}\t\tR$ {}".format (str(a[i]).center(10),n+1, str(b[i]).ljust(10)))
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
        os.system("cls")
 
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
                for i in range(len(produtos_roupas)):
                    print("{}\t\tR$ {}".format(produtos_roupas[i].center(10), str(valores_roupas[i]).ljust(10)))
                    
                print("[0] Voltar para o menu principal")
                print("-"*50)
                print("carrinho de compras",lista_pedido ,sep=" ")
                print("total: R$",sum(lista_valores))
                #funções roupa
                resposta_roupa = int(input(" Por Favor, insira o numero do produto que você deseja !!!!\nProduto:"))
                if resposta_roupa == 1:
            
                    lista_pedido.append(produtos_roupas[0])
                    lista_valores.append(valores_roupas[0])
                elif resposta_roupa == 2:
                    lista_pedido.append(produtos_roupas[1])
                    lista_valores.append(valores_roupas[1])
                elif resposta_roupa == 3:
                    lista_pedido.append(produtos_roupas[2])
                    lista_valores.append(valores_roupas[2])
                elif resposta_roupa == 4:
                    lista_pedido.append(produtos_roupas[3])
                    lista_valores.append(valores_roupas[3])
                elif resposta_roupa == 5:
                    lista_pedido.append(produtos_roupas[4])
                    lista_valores.append(valores_roupas[4])
                elif resposta_roupa == 6 :
                    lista_pedido.append(produtos_roupas[5])
                    lista_valores.append(valores_roupas[5])    
                elif resposta_roupa == 7:
                    lista_pedido.append(produtos_roupas[6])
                    lista_valores.append(valores_roupas[6])
                elif resposta_roupa > 7 or resposta_roupa < 0 :
                    print("Opção Inválida")
                elif resposta_roupa == 0:
                    break

            
            #funções escolares 
            elif resposta_principal == 2:
                os.system("cls")
                print("Escolha o tipo de escolares que deseja adquirir")
                for i in range(len(produtos_escolares)):
                    print("{}\t\tR$ {}".format(produtos_escolares[i].center(10), str(valores_escolares[i]).ljust(10)))
                print("[0] Voltar para o menu principal")
                print("-"*50)
                print(lista_pedido)
                print("total: R$",sum(lista_valores))
                resposta_escolares = int(input(" Por Favor, insira o numero do produto que você deseja !!!!\nProduto:"))
                if resposta_escolares == 1:
                    lista_pedido.append(produtos_escolares[0])
                    lista_valores.append(valores_escolares[0])
                elif resposta_escolares == 2:
                    lista_pedido.append(produtos_escolares[1])
                    lista_valores.append(valores_escolares[1])
                elif resposta_escolares == 3 :
                    lista_pedido.append(produtos_escolares[2])
                    lista_valores.append(valores_escolares[2])
                elif resposta_escolares == 4:
                    lista_pedido.append(produtos_escolares[3])
                    lista_valores.append(valores_escolares[3])
                elif resposta_escolares > 5 or resposta_escolares < 0 :
                    print("Opção Inválida") 
                elif resposta_escolares == 0:
                    break
        
                    #funções comidas 
        
            elif resposta_principal == 3:
                os.system("cls")
                print("Escolha o tipo de produtos que deseja adquirir")
                for i in range(len(produtos_comidas)):
                    print("{}\t\tR$ {}".format(produtos_comidas[i], str(valores_comidas[i]).ljust(10)))
                print("[0] Voltar para o menu principal")
                print("-"*50)
                print(lista_pedido)
                print("total: R$",sum(lista_valores))
                resposta_comidas = int(input(" Por Favor, insira o numero do produto que você deseja !!!!\nProduto:"))
                if resposta_comidas == 1:
                    lista_pedido.append(produtos_comidas[0])
                    lista_valores.append(valores_comidas[0])
                elif resposta_comidas == 2:
                    lista_pedido.append(produtos_comidas[1])
                    lista_valores.append(valores_comidas[1])
                elif resposta_comidas == 3:
                    lista_pedido.append(produtos_comidas[2])
                    lista_valores.append(valores_comidas[2])
                elif resposta_comidas == 4:
                    lista_pedido.append(produtos_comidas[3])
                    lista_valores.append(valores_comidas[3])
                elif resposta_comidas == 5:
                    lista_pedido.append(produtos_comidas[4])
                    lista_valores.append(valores_comidas[4])
                elif resposta_comidas > 5 or resposta_comidas < 0 :
                    print("Opção Inválida")
                elif resposta_comidas == 0:
                    break
            elif resposta_principal > 3 or resposta_principal < 0 :
                print("opção invalida")
            #encerrar o programa e emitir a nota fiscal
        
            elif resposta_principal == 0:
                os.system("cls")
                print("Obrigado por utilizar nossos produtos e nossa loja !!!")
                print("Aqui está sua nota fiscal !\n\n\n\n")
                print("* NOTA FISCAL *")
                print(data_hoje)
                print("nome:",cliente[1], sep=" ")
                print("Endereço:",cliente[3],cliente[5],cliente[4], sep=" ")
                print("CPF/CNPJ:",cliente[2] ,sep=" ")
                print("Cidade: Curitiba")
                print("UF: PR")
                print("CEP:",cliente[6], sep=" ")
                print("-----------------------------")
                print("PRODUTO\t\tPREÇO")
                for i in range(len(lista_pedido)):
                    print("{}\t\tR$ {:.2f}".format(lista_pedido[i], lista_valores[i]))
                print("-----------------------------")
                print("TOTAL:\t\tR$ {:.2f}".format(sum(lista_valores)))
                exit()
                p=0
                break
                

# função de menu principal do lojista
def menu_principal_loja():
    o=1
    while o==1:
        os.system("cls")
        resposta_menu_loja=int(input(f"Olá seja bem vindo ao gerenciamento de estoque\no que você precisa para hoje ?\n[1] - Ver estoque dos produtos\n[2] - ver os gráficos de vendas diarias ou mensais\n[3] - ver gráficos de lucros\n[4] - ver os produtos que estão no varejo\n[5] -  entrar no menu de compras\n[0] -  voltar ao menu de login\nR="))
        while True:
            if resposta_menu_loja == 0:
                return_login()
            elif resposta_menu_loja == 1:
                os.system("cls")
                resposta_menu_produtos=int(input("Quais tipos de produtos você quer conferir ?\n[1]- Produtos roupas\n[2]- Produtos escolares\n[3]-  Produtos Comidas\n[0] voltar\nR="))
                if resposta_menu_produtos == 1:
                    menu_interativo1(pr,vr)
                elif resposta_menu_produtos == 2:
                    menu_interativo1(pe,ve)
                elif resposta_menu_produtos == 3:
                    menu_interativo1(pc,vc)
                elif resposta_menu_produtos > 3 or resposta_menu_produtos < 0:
                    print("opção invalida")
                elif resposta_menu_produtos == 0:
                    break
                elif  resposta_menu_produtos > 5 or resposta_menu_produtos< 0:
                    print("opção incorreta")
            # elif resposta_menu_loja == 2:
        
                    
#login
def login():
    #login no sistema   
    k=1   
    os.system("cls")
    while k==1:
        print("Por favor insira o seu login")
        email_login=str(input("Email:"))
        senha_login=str(input("Senha:"))

        if email_login in email_cliente_db and senha_login in senha_cliente_db: 
            menu_principal_cliente()
            k=0
        elif email_login in email_loja_db and senha_login in senha_loja_db:
            resposta_login_loja=str(input("Você tem cadastro como lojista \nQual menu você deseja ver ?\n[1] Menu cliente\n[2] Menu lojista \nR= "))
            if resposta_login_loja == "1":
                menu_principal_cliente()
                k=0
            elif resposta_login_loja ==  "2":
                menu_principal_loja()
                k=0
            else:
                print("Desculpa, nao consegui entender o seu pedido")
        else:
            print("Login e/ou senha inválidos, tente novamente")


#Verificações 

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

#Verificar cnpj
def verificar_cnpj(cnpj):
    # Remover pontuação do CNPJ
    cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")

    # Verificar se o CNPJ tem 14 dígitos
    if len(cnpj) != 14 or not cnpj.isdigit():
        return False

    # Verificar se todos os dígitos são iguais, o que indica um CNPJ inválido
    if cnpj == cnpj[0] * 14:
        return False

    # Verificar o primeiro dígito verificador
    soma = 0
    peso = 5
    for i in range(12):
        soma += int(cnpj[i]) * peso
        peso = 5 if peso == 2 else peso - 1
    digito_1 = 11 - (soma % 11) if (soma % 11) >= 2 else 0

    if digito_1 != int(cnpj[12]):
        return False

    # Verificar o segundo dígito verificador
    soma = 0
    peso = 6
    for i in range(13):
        soma += int(cnpj[i]) * peso
        peso = 6 if peso == 2 else peso - 1
    digito_2 = 11 - (soma % 11) if (soma % 11) >= 2 else 0

    if digito_2 != int(cnpj[13]):
        return False

    return True


# Função para verificar se uma string contém apenas letras
def verificar_letras(string):
    if not string.replace(" ", "").isalpha():
        print("Entrada inválida. Por favor, insira apenas letras.")
        return False
    return True

# Função para verificar se uma string contém apenas números
def verificar_numeros(string):
    if not string.isdigit():
        print("Entrada inválida. Por favor, insira apenas números.")
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

cliente_teste=0
endereço_teste=0
numero_casa=0
cpf_cnpj=0
complemento_casa=0
cep_teste=0


#lista de produtos para o menu 
produtos_roupas=[
    "Tenis ", "Camisa ", "Jaqueta ", "Calça ","Boné ", "Relogio ","Perfume ",
]
produtos_escolares=[
    "lápis" , "Mochila", "Caneta","Agenda ",]
produtos_comidas=[
    "C/Estudante", "Café", "Refri", "Salgados", "Suco"
]

pr=produtos_roupas
pe=produtos_escolares
pc=produtos_comidas
#Carrinho de compras e o valor total gerado 
lista_pedido=[]
lista_valores=[]


#inicio do codigo




def cadastro():
    z=1
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
def inicio():
    # Perguntar se é um cliente ou lojista
    resposta_inicio = input('''Você é um cliente ou lojista? (Responda "cliente" ou "lojista")\nR: ''')

    while not resposta_inicio:
        print("Resposta vazia. Por favor, responda novamente.")
        resposta_inicio = input('''Você é um cliente ou lojista? (Responda "cliente" ou "lojista")\nR: ''')

    if resposta_inicio.lower() == "cliente":
        # Cadastro de cliente
        resposta_cliente = input('''Você já possui o cadastro de cliente? ("sim" ou "nao")\nR: ''')

        while not resposta_cliente:
            print("Resposta vazia. Por favor, responda novamente.")
            resposta_cliente = input('''Você já possui o cadastro de cliente? ("sim" ou "nao")\nR: ''')

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

            endereco_teste = input("Seu endereço por favor (Sem o número): ")
            while not endereco_teste or not verificar_letras(endereco_teste):
                if not endereco_teste:
                    print("Resposta vazia. Por favor, insira o seu endereço.")
                else:
                    print("Endereço inválido. Por favor, insira um endereço válido.")
                endereco_teste = input("Seu endereço por favor (Sem o número): ")

            complemento_casa = input("Digite um complemento para sua casa: ")
            while not complemento_casa or not verificar_letras(complemento_casa):
                if not complemento_casa:
                    print("Resposta vazia. Por favor, insira um complemento para sua casa.")
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
            while cep_teste and not verificar_cep(cep_teste):
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

            # Inserir os dados do cliente no banco de dados
            cursor.execute('''
                INSERT INTO cliente (nome, cpf_cnpj, endereco, complemento, numero_casa, cep, email, senha)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (cliente_teste, cpf_cnpj, endereco_teste, complemento_casa, numero_casa, cep_teste, registro_cliente_email, registro_cliente_senha))

            conexao.commit()
            print("Cadastro realizado com sucesso!")
            inicio()

        elif resposta_cliente.lower() == "sim":
            print("Você já é nosso cliente. Faça login para continuar.")
            email_cliente = input("Digite seu email: ")
            senha_cliente = input("Digite sua senha: ")

            # Verificar se o email e a senha correspondem a um cliente cadastrado
            cursor.execute('''
                SELECT * FROM cliente WHERE email = ? AND senha = ?
            ''', (email_cliente, senha_cliente))

            cliente = cursor.fetchone()

            if cliente is not None:
                print("Login realizado com sucesso!")
                print("Bem-vindo, {}!".format(cliente[1]))
                menu_principal_cliente(cliente)
            else:
                print("Email ou senha inválidos. Tente novamente.")


    elif resposta_inicio.lower() == "lojista":
        # Cadastro de lojistac
        resposta_lojista = input('''Você já possui o cadastro de lojista? ( "sim" ou "nao" )\nR: ''')

        while not resposta_lojista:
            print("Resposta vazia.Por favor, responda novamente. ")
            resposta_lojista = input('''Você já possui o cadastro de lojista? ( "sim" ou "nao" )\nR: ''')

        if resposta_lojista.lower() == "nao":
            print("Vamos começar o seu cadastro então:")
            # Informações registro do lojista
            lojista_teste = input("Primeiro, por favor insira o seu nome: ")
            while not lojista_teste or verificar_letras(lojista_teste):
                if not lojista_teste :
                    print("Resposta vazia. Por favor, insira o seu nome.")
                else:
                    print("Nome inválido. Por favor, insira um nome válido.")
                lojista_teste = input("Primeiro, por favor insira o seu nome: ")

            cpf_cnpj = input("Em seguida, o seu CPF: ")
            while cpf_cnpj and not verificar_cpf(cpf_cnpj):
                if not cpf_cnpj:
                    print(("Resposta vazia. Por favor, insira o seu CPF."))
                else:
                    print("CPF inválido. Por favor, insira um CPF válido.")
                    cpf_cnpj = input("Em seguida, o seu CPF (Se desejar): ")


            # Verificar se o CPF já está cadastrado
            cursor.execute('''
                SELECT * FROM lojista WHERE cpf_cnpj = ?
            ''', (cpf_cnpj,))
            lojista_existente = cursor.fetchone()

            while lojista_existente:
                print("CPF já cadastrado. Por favor, insira um CPF diferente.")
            cpf_cnpj = input("Em seguida, o seu CPF ou CNPJ: ")
            while cpf_cnpj and not verificar_cpf(cpf_cnpj):
                print("CPF inválido. Por favor, insira um CPF válido.")
                cpf_cnpj = input("Em seguida, o seu CPF: ")


                cursor.execute('''
                    SELECT * FROM lojista WHERE cpf_cnpj = ?
                ''', (cpf_cnpj,))
                lojista_existente = cursor.fetchone()

            endereco_teste = input("Seu endereço por favor (Sem o número): ")
            while not verificar_letras(endereco_teste):
                endereco_teste = input("Seu endereço por favor (Sem o número): ")

            complemento_casa = input("Digite um complemento para sua casa: ")
            while not verificar_letras(complemento_casa):
                complemento_casa = input("Digite um complemento para sua casa: ")

            numero_casa = input("Agora insira o número: ")
            while not verificar_numeros(numero_casa):
                numero_casa = input("Agora insira o número: ")

            cep_teste = input("Insira o CEP (Somente números): ")
            while cep_teste and not verificar_cep(cep_teste):
                print("CEP inválido.Por favor, insira um CEP válido.")
                cep_teste = input("Insira o CEP (Somente números): ")

            registro_lojista_email = input("Digite o seu email: ")
            while not verificar_email(registro_lojista_email):
                print("Email inválido.Por favor, insira um Email válido.")
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
            print("Você já é nosso lojista. Faça login para continuar.")
            email_lojista = input("Digite seu email: ")
            senha_lojista = input("Digite sua senha: ")

            # Verificar se o email e a senha correspondem a um lojista cadastrado
            cursor.execute('''
                SELECT * FROM lojista WHERE email = ? AND senha = ?
            ''', (email_lojista, senha_lojista))

            lojista = cursor.fetchone()

            if lojista is not None:
                print("Login realizado com sucesso!")
                print("Bem-vindo, {}!".format(lojista[1]))
                menu_principal_loja()            
            else:
                print("Email ou senha inválidos. Tente novamente.")

    conexao.close()

inicio()

