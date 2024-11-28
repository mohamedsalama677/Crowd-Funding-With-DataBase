import mysql.connector

def login(email,password):
    conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "salama97",
    database = "Authentication_System"
    )
    if isinstance(email,str) and isinstance(password,str):
        cursor = conn.cursor()
        query_add = """
                    select ID,Fname,Lname,Phone,proTitle,hours
                    from users as u ,work_in as w
                    where binary u.ID = w.userID and binary u.Email = %s and u.pass = %s;
                    """
        values = (email,password)
        cursor.execute(query_add, values)
        result = cursor.fetchall() 
        conn.commit()
    cursor.close()
    conn.close()
    return result  
