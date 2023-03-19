'''
Crie um script contendo cinco funções:
    1. Criar itens, onde o usuário pode selecionar a quantidade de campos;
    2. Mostrar todos os documentos;
    3. Deletar documentos pelo ID;
    4. Deletar toda a coleção do banco de dados;
    5. Atualizar documentos por ID ou por campos.
OBS: Não precisa criar menu para escolha das funções, elas podem ser chamadas separadamente.
'''
# 1. Criar itens, onde o usuário pode selecionar a quantidade de campos;
from pymongo import collection

def conectar_mongodb():
    from pymongo import MongoClient
    CONNECTION_STRING = "mongodb+srv://madson:minhasenha@clustercurso.ldamgvm.mongodb.net/?retryWrites=true&w=majority"
    cliente = MongoClient(CONNECTION_STRING)
    print("Base de dados conectada com sucesso. \n")
    return cliente["exercicio_4"]

def criar_documento():
    minha_base_dados = conectar_mongodb()
    exercicio_4 = minha_base_dados["exercicio_4"]
    quantidade_itens_digitadas_usuario = int(input("Digite a quantidade de itens que seu documento terá: "))
    dicionario = dict(input("Digite a chave e o valor. Deve haver dois pontos(':')separando-os: ").split(':') for _ in range(quantidade_itens_digitadas_usuario))
    print(dicionario)
    exercicio_4.insert_one(dicionario)
    print("Seu documento foi inserido com sucesso. ")
criar_documento()
criar_documento()
criar_documento()
criar_documento()
criar_documento()

# 2. Mostrar todos os documentos;
def mostrar_todos_documentos():
    minha_base_dados = conectar_mongodb()
    exercicio_4 = minha_base_dados["exercicio_4"]
    exibir_itens_documentos = exercicio_4.find()
    for item in exibir_itens_documentos:
        print(item)
mostrar_todos_documentos()

# 3. Deletar documentos pelo ID;
def deletar_documentos_ID():
    minha_base_dados = conectar_mongodb()
    exercicio_4 = minha_base_dados["exercicio_4"]
    documentos_deletados_usuario = str(input("Qual o ID do item que você quer deletar? "))
    exercicio_4.delete_one({"_id":documentos_deletados_usuario})
    print("Documento(s) deletado(s) com sucesso. ")
deletar_documentos_ID()

# 4. Deletar toda a coleção do banco de dados;

def deletar_toda_colecao_banco():
    confirmar_exclusao = str(input("Você realmente deseja apagar tudo? Digite SIM para CONFIRMAR ou NÃO para CANCELAR: ").upper())
    minha_base_dados = conectar_mongodb()
    exercicio_4 = minha_base_dados["exercicio_4"]
    if (confirmar_exclusao == "SIM"):
        exercicio_4.drop()
        minha_base_dados.drop_collection()
        print("Coleção deletada com sucesso. ")
    elif (confirmar_exclusao == "NÃO"):
        print("Não houve exclusão de dados. ")
    else:
        print("")
deletar_toda_colecao_banco()

# 5. Atualizar documentos por ID ou por campos.
def atualizar_documentos():
    minha_base_dados = conectar_mongodb()
    exercicio_4 = minha_base_dados["exercicio_4"]
    opcao_escolhida = str(input("Você quer atualizar os documentos por ID ou por campos? (Digite ID caso queira atualizar por ID ou digite CAMPO caso queira atualizar por CAMPOS) ").upper())
    if (opcao_escolhida == "ID"):
        id = str(input("Digite o ID que você deseja modificar: "))
        chave = str(input("Digite o campo que você deseja modificar: "))
        valor = str(input("Digite o novo valor do campo: "))
        exercicio_4.update_one({"_id":id}, {"$set":{chave:valor}})
        print("ID alterado com sucesso. ")
    elif (opcao_escolhida == "CAMPO"):
        chave_alterada = str(input("Digite a chave que você deseja alterar: "))
        nova_chave = str(input("Digite o novo campo que substituirá a chave antiga que você digitou para alterá-la: "))
        valor_alterado = str(input("Digite o valor que você deseja alterar: "))
        novo_valor = str(input("Digite o novo valor que substituirá o valor antigo que você digitou para alterá-lo: "))
        exercicio_4.update_many({chave_alterada:valor_alterado}, {"$set":{nova_chave:novo_valor}})
        print("As alterações foram realizadas com sucesso. ")
atualizar_documentos()
mostrar_todos_documentos()