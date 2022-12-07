import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ac018411.',
    database='projeto-mentoria',
)

cursor = conexao.cursor()

# CRUD - etapas

# CREATE

# produto = "pulseira"
# quantidade = 5
# cursor.execute(f'INSERT INTO estoque (produto, quantidade) VALUES ("{produto}", {quantidade})')
# conexao.commit() #usado para editar BD (create, update ou delete)

# READ

# cursor.execute(f'SELECT * FROM estoque')
# resultado = cursor.fetchall() #ler o banco de dados
# print(resultado)

# UPDATE

# produto = "colar"
# quantidade = 10
# cursor.execute(f'UPDATE estoque SET quantidade = {quantidade} WHERE produto = "{produto}"')
# conexao.commit()

# DELETE

# produto = "pulseira"
# cursor.execute(f'DELETE FROM estoque WHERE produto = "{produto}"')
# conexao.commit()


cursor.close()
conexao.close()


