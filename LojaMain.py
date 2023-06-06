from datetime import date
import re
import os
# a fazer ainda !!!!!!!!!!! cadastro de itens, terminar menu de lojista




#Variavel para estrutura de repetição infinita 
z=1



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
def menu_principal_cliente():
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
                print("nome:",cliente_teste, sep=" ")
                print("Endereço:",endereço_teste,numero_casa,complemento_casa, sep=" ")
                print("CPF/CNPJ:",cpf_cnpj ,sep=" ")
                print("Cidade: Curitiba")
                print("UF: PR")
                print("CEP:",cep_teste, sep=" ")
                print("-----------------------------")
                print("PRODUTO\t\tPREÇO")
                for i in range(len(lista_pedido)):
                    print("{}\t\tR$ {:.2f}".format(lista_pedido[i], lista_valores[i]))
                print("-----------------------------")
                print("TOTAL:\t\tR$ {:.2f}".format(sum(lista_valores)))
                p=0
                break

# função de menu principal do lojista
def menu_principal_loja():
    o=1
    while o==1:
        os.system("cls")
        resposta_menu_loja=str(input(f"Olá seja bem vindo ao gerenciamento de estoque\no que você precisa para hoje ?\n[1] - Ver estoque dos produtos\n[2] - adicionar itens do estoque para venda\n[3] - ver os gráficos de vendas diarias ou mensais\n[4] - ver gráficos de lucros\n[5] - ver os produtos que estão no varejo\n[6] -  entrar no menu de compras\n[0] -  voltar ao menu de login\nR="))
        while True:
            if resposta_menu_loja == "1":
                os.system("cls")
                resposta_menu_produtos=str(input("Quais tipos de produtos você quer conferir ?\n[1]- Produtos roupas\n[2]- Produtos escolares\n[3]-  Produtos Comidas\n[0] voltar\nR="))
                if resposta_menu_produtos == "1":
                    menu_interativo1(pr,vr)
                elif resposta_menu_produtos == "2":
                    menu_interativo1(pe,ve)
                elif resposta_menu_produtos == "3":
                    menu_interativo1(pc,vc)

        
                    
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
    #Remover pontuação do CNPJ
    cnpj = cnpj.replace(".","").replace("/","").replace("-","")

    #Verficar se o CNPJ tem 14 dígitos
    if len(cnpj) != 14 or not cnpj.isdigit():
        return False
    
    #Verificar se todos os dígitos são iguais, o que indica um CNPJ inválido
    if cnpj == cnpj[0] * 14:
        return False
    
    #Verificar o primeiro dígito verificador
    soma = sum(int(cnpj[i]) * (5 - i if i < 5 else 13 - 1) for i in range(12))
    digito_1 = (soma % 11)
    if digito_1 < 2:
        digito_1 = 0
    else:
        digito_1 == 11 - digito_1

    if digito_1 != int(cnpj[12]):
        return False
    

    #Verificar o segundo dígito verificador
    soma = sum(int(cnpj[i]) * (6 - i if i < 6 else 14 - i) for i in range(13))
    digito_2 = (soma % 11)
    if digito_2 < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - digito_2

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




# frase inicial 
os.system("cls")
print("Olá SEJA BEM VINDO a loja  da PUCPR \nVamos iniciar o seu atendimento personalizado")


#cliente ou lojista
resposta_inicio=str(input("""
Primeiro precisamos saber se você deseja ser um cliente \nou se você deseja vender seus itens em nossa loja 

Digite cliente para iniciar o seu cadastro como cliente 
Digite lojista para iniciar o seu cadastro como lojista

R : """))
os.system("cls")
while z == 1:
    if resposta_inicio.lower() == "cliente":
        # Cadastro de cliente
        resposta_cliente = str(input("Você já é cliente de nossa loja?\n\nR: "))
        if resposta_cliente.lower() == "nao":
            print("Vamos começar o seu cadastro então:")
            # Informações do cliente
            cliente_teste = input("Primeiro, por favor insira o seu nome: ")
            while not verificar_letras(cliente_teste):
                cliente_teste = input("Nome inválido, por favor insira o seu nome corretamente: ")

            cpf_cnpj = input("Em seguida, o seu CPF/CNPJ (Se desejar): ")

            # Verificação do CPF
            while cpf_cnpj and not verificar_cpf(cpf_cnpj):
                print("CPF inválido. Por favor, insira um CPF válido.")
                cpf_cnpj = input("Em seguida, o seu CPF/CNPJ (Se desejar): ")

            endereço_teste = input("Seu endereço por favor (Sem o número): ")
            while not verificar_letras(endereço_teste):
                print("Endereço inválido. Por favor, insira um Endereço válido.")
                endereço_teste = input("Seu endereço por favor (Sem o número): ")

            complemento_casa = input("Seu complemento (Casa, apto, etc.): ")
            while not verificar_letras(complemento_casa):
                print("Complemento inválido. Por favor, insira um complemento válido.")
                complemento_casa = input("Seu complemento (Casa, apto, etc.): ")

            numero_casa = input("Seu número da casa: ")
            while not verificar_numeros(numero_casa):
                print("Número inválido. Por favor, insira um número válido.")
                numero_casa = input("Seu número da casa: ")

            cep_teste = input("Seu CEP: ")
            while not verificar_cep(cep_teste):
                print("CEP inválido. Por favor, insira um CEP válido.")
                cep_teste = input("Seu CEP: ")

            registro_cliente_email = str(input("Digite seu email: "))
            while not verificar_email(registro_cliente_email):
                print("Email inválido. Por favor, insira um Email válido.")
                registro_cliente_email = input("Digite seu email: ")

            registro_cliente_senha = str(input("Digite a senha: "))
            email_cliente_db.append(registro_cliente_email)
            senha_cliente_db.append(registro_cliente_senha)
            z = 0
        elif resposta_cliente.lower() == "sim":
            z = 0
            pass
    elif resposta_inicio.lower() == "lojista":
        resposta_lojista = str(input("Você já possui o cadastro de lojista? "))
        if resposta_lojista.lower() == "nao":
            print("Vamos começar o seu cadastro então:")
            # Informações do cliente
            cliente_teste = input("Primeiro, por favor insira o seu nome: ")
            while not verificar_letras(cliente_teste):
                cliente_teste = input("Nome inválido, por favor insira o seu nome corretamente: ")

            cpf_cnpj = input("Em seguida, o seu CPF/CNPJ (Se desejar): ")
            while cpf_cnpj and not verificar_cpf(cpf_cnpj):
                print("CPF inválido. Por favor, insira um CPF válido.")
                cpf_cnpj = input("Em seguida, o seu CPF/CNPJ (Se desejar): ")

            endereço_teste = input("Seu endereço por favor (Sem o número): ")
            while not verificar_letras(endereço_teste):
                print("Endereço inválido. Por favor, insira um Endereço válido.")
                endereço_teste = input("Seu endereço por favor (Sem o número): ")

            complemento_casa = input("Seu complemento (Casa, apto, etc.): ")
            while not verificar_letras(complemento_casa):
                print("Complemento inválido. Por favor, insira um complemento válido.")
                complemento_casa = input("Seu complemento (Casa, apto, etc.): ")

            numero_casa = input("Seu número da casa: ")
            while not verificar_numeros(numero_casa):
                print("Número inválido. Por favor, insira um número válido.")
                numero_casa = input("Seu número da casa: ")

            cep_teste = input("Seu CEP: ")
            while not verificar_cep(cep_teste):
                print("CEP inválido. Por favor, insira um CEP válido.")
                cep_teste = input("Seu CEP:")


            registro_loja_email = str(input("Digite seu email: "))
            while not verificar_email(registro_loja_email):
                print("Email inválido. Por favor, insira um Email válido.")
                registro_loja_email = input("Digite seu email: ")
            registro_loja_senha = str(input("Digite a senha: "))
            email_loja_db.append(registro_loja_email)
            senha_loja_db.append(registro_loja_senha)
            z = 0
        elif resposta_lojista.lower() == "sim":
            z = 0

#login no sistema      
login()