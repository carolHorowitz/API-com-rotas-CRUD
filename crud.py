import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ac018411.',
    database='projeto-mentoria',
)

cursor = conexao.cursor()



cursor.close()
conexao.close()


