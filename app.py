import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn=psycopg2.connect("postgres://lab_10_cspb_3308_database_user:QyGIpeJXm5FAO3CqkdvykoTXfNpLFRL2@dpg-cgkaoqe4dad69r1ngi60-a/lab_10_cspb_3308_database")
    conn.close()
    return "Database Connection Successful."

@app.route('/db_create')
def creating():
    conn=psycopg2.connect("postgres://lab_10_cspb_3308_database_user:QyGIpeJXm5FAO3CqkdvykoTXfNpLFRL2@dpg-cgkaoqe4dad69r1ngi60-a/lab_10_cspb_3308_database")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created."


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
