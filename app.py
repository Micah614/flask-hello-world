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
    return "Basketball Table Successfully Created!"


@app.route('/db_insert')
def inserting():
    conn=psycopg2.connect("postgres://lab_10_cspb_3308_database_user:QyGIpeJXm5FAO3CqkdvykoTXfNpLFRL2@dpg-cgkaoqe4dad69r1ngi60-a/lab_10_cspb_3308_database")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated!"


@app.route('/db_select')
def selecting():
    conn=psycopg2.connect("postgres://lab_10_cspb_3308_database_user:QyGIpeJXm5FAO3CqkdvykoTXfNpLFRL2@dpg-cgkaoqe4dad69r1ngi60-a/lab_10_cspb_3308_database")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Basketball;''')
    records = cursor.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</tables>"
    return response_string
    
    