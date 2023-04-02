import psycopg2
from flask import Flask
# from flask_table import Table, Col
app = Flask(__name__)

# # declare the table.
# class ItemTable(Table):
#     first = Col('First')
#     last = Col('Last')
#     city = Col('City')
#     name = Col('Name')
#     number = Col('Number')

# populate it with objects.
# class Table(records):
#     def __init__(self, first, last, city, name, number):
#         # 
#         self.first = first
#         self.last = last
#         self.city = city
#         self.name = name
#         self.number = number
#         # 
#         items = records.query.all()
        
#         # Populate the table
#         table = ItemTable(items)

#         # Print the html
#         print(table.__html__())

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
    # return render_template('table.html', data=records)
    return render_template('table.html', data=records)
    conn.commit()
    conn.close()
    
