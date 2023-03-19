'''
Crie um script contendo as instruções abaixo:

1.    Crie uma base de dados chamada sistema_escolar_soul_on

2.    Crie uma tabela alunos com os campos id, nome, matricula, turma.

3.    Alimente a tabela com os seguintes dados:



4.    Faça as seguintes consultas:

·    Liste todos os registros de sua tabela.

·    Liste apenas nome e matrícula dos alunos do BCW23.

·    Liste apenas o nome dos alunos que tiverem o sobrenome Lima.

 

5.    O aluno Carlos Augusto está na turma errada. Matricule o mesmo no BCW25.

6.    O aluno José Vinicius desistiu do curso, ele deve ser excluído do sistema.

 

*Se preferir, pode usar funções para evitar exclusões.
'''

import mysql.connector

# 1)
def criar_base_dados():
    base_dados = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ""
    )

    meu_cursor = base_dados.cursor()
    meu_cursor.execute("CREATE DATABASE sistema_escolar_soul_on")
    print("A base de dados foi criada. ")
print("1. Crie uma base de dados chamada sistema_escolar_soul_on")
criar_base_dados()
print("\n")

base_dados = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "sistema_escolar_soul_on"
)

meu_cursor = base_dados.cursor()

# 2)
def criar_tabela():
    meu_cursor.execute("CREATE TABLE alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), matricula VARCHAR(255), turma VARCHAR(255))")
    print("Tabela criada com sucesso. ")
print("2. Crie uma tabela alunos com os campos id, nome, matricula, turma.")
criar_tabela()
print("\n")

# 3)
def inserir_dados():
    sql = "INSERT INTO alunos (nome, matricula, turma) VALUES (%s, %s, %s)"
    val = [
        ('José Lima', 'MAT90551', 'BCW22'), 
        ('Carlos Augusto', 'MAT90552', 'BCW22'),
        ('Lívia Lima', 'MAT90553', 'BCW22'),
        ('Sandra Gomes', 'MAT90554', 'BCW23'),
        ('João Augusto', 'MAT90555', 'BCW23'),
        ('Breno Lima', 'MAT90556', 'BCW24'),
        ('José Vinícius', 'MAT90557', 'BCW25')
    ]
    meu_cursor.executemany(sql, val)
    base_dados.commit()
    print(meu_cursor.rowcount, "linha(s) inserida(s) na base de dados. ")
print("3. Alimente a tabela com os seguintes dados: (Obs.: os dados estão contidos em uma imagem, portanto não tenho como colocá-los aqui.)")
inserir_dados()
print("\n")

# 4)
# Liste todos os registros de sua tabela.
def consultar_dados1():
    meu_cursor.execute("SELECT * FROM alunos")
    resultados = meu_cursor.fetchall()
    for x in resultados:
        print(x)
print("Liste todos os registros de sua tabela.")
consultar_dados1()
print("\n")

# Liste apenas nome e matrícula dos alunos do BCW23.
def consultar_dados2():
    meu_cursor.execute("SELECT nome, matricula FROM alunos WHERE turma = 'BCW23'")
    resultados = meu_cursor.fetchall()
    for x in resultados:
        print(x)
print("Liste apenas nome e matrícula dos alunos do BCW23.")
consultar_dados2()
print("\n")

# Liste apenas o nome dos alunos que tiverem o sobrenome Lima.
def consultar_dados3():
    meu_cursor.execute("SELECT nome FROM alunos WHERE nome LIKE '%Lima%'")
    resultados = meu_cursor.fetchall()
    for x in resultados:
        print(x)
print("Liste apenas o nome dos alunos que tiverem o sobrenome Lima.")
consultar_dados3()
print("\n")

# 5)
def trocar_turma():
    sql = "UPDATE alunos SET turma = 'BCW25' WHERE id = '2'"
    meu_cursor.execute(sql)
    base_dados.commit()
    print(meu_cursor.rowcount, "linha(s) alterada(s). ")
print("5. O aluno Carlos Augusto está na turma errada. Matricule o mesmo no BCW25.")
trocar_turma()
print("\n")

# 6) 
def excluir_aluno():
    sql = "DELETE FROM alunos WHERE id = '7'"
    meu_cursor.execute(sql)
    base_dados.commit()
    print(meu_cursor.rowcount, "linha(s) deletada(s). ")
print("6. O aluno José Vinicius desistiu do curso, ele deve ser excluído do sistema.")
excluir_aluno()
print("\n")