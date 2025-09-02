import mysql.connector
from flask import jsonify


def conexão():
    con = mysql.connector.connect(host = 'localhost', database = 'db_urlshort', user = 'root', password = 'root')

    return con

def get_lista():
    con = None
    cursor = None
    try:
        con = conexão()
        cursor = con.cursor()

        cursor.execute("select * from url")
        myresult = cursor.fetchall()

        return jsonify(myresult)
    
    except mysql.connector.Error as erro:

        print('Erro ao executar a query', erro)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
        

def post_url(url_long, url_new):
    con = None
    cursor = None
    try:
        con = conexão()
        cursor = con.cursor()

        query = 'INSERT INTO url (url_org, url_short, count_click) VALUES (%s, %s, %s)'
        data = (url_long, url_new, 0)
        cursor.execute(query, data)
        con.commit()

        return 'http://127.0.0.1:5000/get/' + url_new
    
    except mysql.connector.Error as erro:

        print('Erro ao executar a query', erro)

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def get_link(url):
    con = None
    cursor = None
    try:
        con = conexão()
        cursor = con.cursor()

        data = (url,)
        cursor.execute(
            'SELECT url_org FROM url WHERE url_short = %s', data
        )
        resultado = cursor.fetchone()  # consome o resultado

        if resultado:
            incrementa(url)
            return resultado[0]
        else:
            return None

    except mysql.connector.Error as erro:
        print('Erro ao executar a query:', erro)
        return erro

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
        
def incrementa(url):

    con = None
    cursor = None

    try:
        con = conexão()
        cursor = con.cursor()

        data = (url,)
        cursor.execute(
            'SELECT count_click FROM url WHERE url_short = %s', data
        )
        resultado = cursor.fetchone()

        count = list(resultado)
        count[0] += 1
        count_click(count[0], url)

    except mysql.connector.Error as erro:

        print('Erro ao executar a query:', erro)
        return None
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

    return resultado

def count_click(result, url):
    con = None
    cursor = None

    try:
        con = conexão()
        cursor = con.cursor()

        data = (result, url)
        cursor.execute(
            'UPDATE url SET count_click = %s  WHERE url_short = %s', data
        )
        
        con.commit()
    except mysql.connector.Error as erro:

        print('Erro ao executar a query:', erro)
        return None
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()