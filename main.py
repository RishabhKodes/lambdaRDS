import pymysql
import sys

REGION = 'us-east-1f'

rds_host  = "rds_endpoint"
name = "master_username"
password = "master_password"
db_name = "dbInstance_name"

def save_events(event):
    """
    This function fetches content from mysql RDS instance
    """
    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into test (id, name) values( %s, '%s')""" % (event['id'], event['name']))
        cur.execute("""select * from test""")
        # cur.execute("""TRUNCATE TABLE test;""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print("Data from RDS...")
        print(result)

def main(event, context):
    save_events(event)

event = {
  "id": "1",
  "name": "Elon Musk"
}
context = "" 
main(event, context)