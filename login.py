import sqlite3

location = 'database.db'

def init():    
    global conn
    global c
    conn = sqlite3.connect(location)
    c = conn.cursor()
    create_database()

def create_database():
    c.execute('create table if not exists logindb (login, password)')
    conn.commit()


def clear_database():
    c.execute('drop table logindb')
    conn.commit()

def commit():
    conn.commit()

def close():
    conn.close()


def exists(values):
    c.execute('SELECT * FROM logindb WHERE login=?', values)
    
    return c.fetchone()

def insert(values):
    c.execute("insert into logindb values (?, ?)", values)

def search(values):
    c.execute('SELECT * FROM logindb WHERE login=? AND password=?', values)
    return c.fetchone()


def signup(login, password):
    init()
    if exists((login,)) :
        close()
        return False
    else:
        insert((login,password))
        commit()
        res = search((login,password)) 
        close()
        return res


def signin(login, password):
    init()
    result = search((login,password)) 
    close()
    return result


