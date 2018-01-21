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
