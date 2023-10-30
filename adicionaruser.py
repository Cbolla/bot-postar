from dotenv import load_dotenv
from dotenv import load_dotenv
import MySQLdb
import os


# conectando ao banco
load_dotenv()

db_host = os.getenv("DATABASE_HOST")
db_username = os.getenv("DATABASE_USERNAME")
db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE")

if db_host is None or db_username is None or db_password is None or db_name is None:
    print("Alguma das variáveis de ambiente não está configurada corretamente.")
else:
    connection = MySQLdb.connect(
        host=db_host,
        user=db_username,
        passwd=db_password,
        db=db_name,
        autocommit=True,
        ssl_mode="VERIFY_IDENTITY",
        ssl={
            "ca": "cacert-2023-08-22.pem",
            "usepure": True
        }
    )
  
  # Dados do usuário a ser inserido
email = "futuro.noob@gmail.com"
senha = "1234"
nome = "cbolla"
# fim
# Crie um cursor
cursor = connection.cursor()

# Execute a consulta SQL para adicionar um novo usuário
sql = "INSERT INTO usuarios (email, senha, nome) VALUES (%s, %s, %s)"
values = (email, senha, nome)

cursor.execute(sql, values)

# Faça commit para confirmar a transação
connection.commit()

print("Usuário adicionado com sucesso!")

# Feche o cursor e a conexão
cursor.close()
connection.close()
