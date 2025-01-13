import MySQLdb

def create_connection():
    conn= conn = MySQLdb.connect(
        host="Localhost",
        user="root",
        password="Harsh@2004",
        database="sales_data"
    )
    return conn