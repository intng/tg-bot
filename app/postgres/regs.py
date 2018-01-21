import os, psycopg2

import urllib.parse

result = urllib.parse.urlparse(os.getenv("postgres_uri"))
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname


def check_reg(token):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            select = "SELECT * FROM regs WHERE token = %s"
            cur.execute(select, (token,))
            res = cur.fetchall()
            if res:
                return res[0]
            else:
                return False


def del_reg(token):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            delete = "DELETE FROM regs WHERE token = %s"
            cur.execute(delete, (token,))
            conn.commit()
            return True


def new_reg(token):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            insert = "INSERT INTO regs (token) VALUES (%s)"
            cur.execute(insert, (token,))
            conn.commit()
            return True

def update(id, name, token, surname=None):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            update = "UPDATE regs SET id = %s, name = %s, surname = %s WHERE token = %s"
            cur.execute(update, (id, name, surname, token))
            conn.commit()
            return True
