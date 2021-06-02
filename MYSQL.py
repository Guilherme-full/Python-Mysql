import mysql.connector
from mysql.connector import Error


def envio_de_dados(host_, database_, user_, senha_, id_au, nome_,sobre, concatenacao):
     try:
         con = mysql.connector.connect(host=host_, database=database_, user=user_, password=senha_)
         inserir_produtos = sql
         cursor = con.cursor()
         cursor.execute(inserir_produtos)
         con.commit()
         print(cursor.rowcount, 'Registros inseridos na tabela!')
         cursor.close()
     except Error as erro:
         print(f'Falha ao inserir dados no MYSQL: {erro}')
     finally:
         if (con.is_connected()):
             cursor.close()
             con.close()
             print('Conexão finalizada !')

print('Cadastro de Informações no banco de dados')
print('Olá usario, entre com os dados solicitados')

hos = input('Informe seu host: ')
banco = input('Informe o nome do seu banco de dados: ')
usu = input('Informe seu úsuario: ')
sen = input('Informe sua senha: ')
idpro = input('id do autor: ')
nomeProd = input('Nome do autor: ')
precoProd = input('Sobrenome do autor: ')
dados = idpro + ',\'' + nomeProd + '\',\'' + precoProd + '\')'
declaracao = '''insert into tbl_autores
(ID_autor, Nome_Autor, Sobrenome_Autor)
values ('''
sql = declaracao + dados
envio_de_dados(hos, banco , usu, sen, idpro, nomeProd, precoProd, sql)