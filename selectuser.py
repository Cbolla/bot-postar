import MySQLdb
import os
from dotenv import load_dotenv

# Conectando ao banco
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

    cursor = connection.cursor()

    # Execute a consulta SQL para selecionar todos os registros da tabela "usuarios"
    sql = "SELECT * FROM usuarios"

    cursor.execute(sql)

    # Recupere todos os resultados da consulta
    results = cursor.fetchall()

    # Imprima os resultados
    for row in results:
        print("ID:", row[0])
        print("Nome:", row[1])
        print("Email:", row[2])
        # Adicione mais campos conforme necessário

    # Feche o cursor e a conexão
    cursor.close()
    connection.close()
