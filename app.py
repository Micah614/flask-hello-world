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


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
