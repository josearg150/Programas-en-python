import mysql.connector

bd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='pruebas'
)

cursor = bd.cursor()

#sql = 'insert into usuario (id,email, username, edad) values (%s,%s,%s,%s)'
#values = (3,'angel@pruebas.com', 'angel12', 20)

#cursor.execute(sql, values)
#bd.commit()
#print(cursor.rowcount)
cursor.execute('SELECT * FROM usuario limit 1')
#cursor.execute('show create table usuario')

result = cursor.fetchall()

#actualizar datos
#sql = 'update usuario set email = %s  where id = %s'
#values = ('angelangel@pruebas.co',3)

#cursor.execute(sql, values)
#bd.commit()

#eliminar datos

#sql = 'delete from usuario where id = %s'
# values = (3, )
# cursor.execute(sql, values)
# bd.commit()
print(result)