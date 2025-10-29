import psycopg2

def connection_db():
    conn = psycopg2.connect(
        database="control",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    return conn