import mysql.connector
def ID():
    conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "salama97",
    database = "Authentication_System"
    )
    cursor = conn.cursor()
    query_id = "select max(ID) as max_ID from users"
    cursor.execute(query_id)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
def add_row(row):
    conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "salama97",
    database = "Authentication_System"
    )
    if isinstance(row,tuple):
        cursor = conn.cursor()
        query_add = "insert into users (ID,Fname,Lname,Email,pass,Phone) values (%s,%s,%s,%s,%s,%s)"
        values = row
        cursor.execute(query_add, values)
        conn.commit()
        print("your data are saved")
    cursor.close()
    conn.close()
conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "salama97",
    database = "Authentication_System"
    )

