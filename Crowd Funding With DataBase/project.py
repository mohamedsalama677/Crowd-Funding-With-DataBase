import mysql.connector

def proj_manger(email,passw):
    conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "salama97",
    database = "Authentication_System"
    )
    
    cursor = conn.cursor()
    query_add = """
                select Title,Details,Total_target,Start_date,End_date,Manger
                from projects
                where Manger = (select ID from users where Email = %s and pass = %s);
                """
    values = email,passw
    cursor.execute(query_add, values)
    result = cursor.fetchall()
    result = [(row[0],row[1],row[2],row[3].strftime('%Y-%m-%d'),row[4].strftime('%Y-%m-%d'),row[5]) for row in result]
    conn.commit()
    cursor.close()
    conn.close()
    return result


def add_proj(title,detalis,tot,st_date,en_date,mang):
            
    
        
        try:
            conn = mysql.connector.connect(
                    host ="localhost",
                    user = "root",
                    password = "salama97",
                    database = "Authentication_System"
                    )
            cursor = conn.cursor()
            query_add = """
                    insert into projects (Title, Details, Total_target, Start_date, End_date,Manger)
                    values (%s,%s,%s,%s,%s,%s); 
                    """
            values = title,detalis,tot,st_date,en_date,mang
            cursor.execute(query_add, values)
            conn.commit()
            cursor.close()
            conn.close()
            return 1
        except:
            return 0
    
    
        
    


    
def show_all():
    conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "salama97",
    database = "Authentication_System"
    )
    
    cursor = conn.cursor()
    query_add = """
                select * from projects;
                """
    
    cursor.execute(query_add)
    result = cursor.fetchall()
    result = [(row[0],row[1],row[2],row[3].strftime('%Y-%m-%d'),row[4].strftime('%Y-%m-%d'),row[5]) for row in result]
    conn.commit()
    cursor.close()
    conn.close()
    return result


def delete_proj(title):
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "salama97",
        database = "Authentication_System"
        )
    cursor = conn.cursor()
    query_del_1 = """
              
                delete from work_in where proTitle = %s;
                
                """
    values = (title,)
    cursor.execute(query_del_1, values)
    query_del_2 = """ 
                    delete from projects where Title = %s;

                  """
    values2 = (title,)
    cursor.execute(query_del_2,values2) 
    conn.commit()
    cursor.close()
    conn.close()



def edit_proj(title,details,tot,st_date,en_date,ID):
    try:
        conn = mysql.connector.connect(
                    host ="localhost",
                    user = "root",
                    password = "salama97",
                    database = "Authentication_System"
                    )
        cursor = conn.cursor()
        query_add = """
                update projects 
                set Title = %s,Details =%s ,Total_target =%s ,Start_date =%s,End_date =%s 
                where Title = %s
                """
        values = title,details,tot,st_date,en_date,title
        cursor.execute(query_add, values)
        conn.commit()
        cursor.close()
        conn.close()
        return 1
    except:
        return 0



def search_stdate(stdate):
    conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "salama97",
    database = "Authentication_System"
    )
    
    cursor = conn.cursor()
    query_add = """
                select * from projects
                where Start_date = %s
                """
    value = (stdate,)
    cursor.execute(query_add,value)
    result = cursor.fetchall()
    result = [(row[0],row[1],row[2],row[3].strftime('%Y-%m-%d'),row[4].strftime('%Y-%m-%d'),row[5]) for row in result]
    cursor.close()
    conn.close()
    return result

def search_endate(endate):
    conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "salama97",
    database = "Authentication_System"
    )
    
    cursor = conn.cursor()
    query_add = """
                select * from projects
                where End_date = %s
                """
    value = (endate,)
    cursor.execute(query_add,value)
    result = cursor.fetchall()
    result = [(row[0],row[1],row[2],row[3].strftime('%Y-%m-%d'),row[4].strftime('%Y-%m-%d'),row[5]) for row in result]
    cursor.close()
    conn.close()
    return result


