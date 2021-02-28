import pyodbc

def __getDatabaseConnetion():
    return pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=localhost\\SQLEXPRESS;Databse=master;Trusted_Connection=yes;")

def insertBooks(bookName,rating,price):
    with __getDatabaseConnetion() as conn:
        cursor = conn.cursor()
        bookName = bookName.replace("'","''")
        insert_sql = f"insert into TblBooks(name,rating,price) values('{bookName.strip()}',{rating},'{price.strip()}')"
        cursor.execute(insert_sql)

def clearBooks():
    with __getDatabaseConnetion() as conn:
        cursor = conn.cursor()
        delete_sql = f"Truncate table TblBooks"
        cursor.execute(delete_sql)