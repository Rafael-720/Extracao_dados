import pandas as pd
import psycopg2
import mysql.connector
import fdb
# Importe as bibliotecas necessárias para Firebird, SQL Server, Oracle

def connect_to_postgres(query, host, port, user, password, db):
    conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=db)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def connect_to_mysql(query, host, port, user, password, db):
    conn = mysql.connector.connect(host=host, port=port, user=user, password=password, database=db)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Adicione funções para Firebird, SQL Server, Oracle aqui, incluindo a porta nas conexões
def connect_to_firebird(query, host, port, user, password, db):
    conn = fdb.connect(database=db, host=host, port=port, user=user, password=password)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df