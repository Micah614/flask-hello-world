import psycopg2
from flask import Flask
# from flask_table import Table, Col
app = Flask(__name__)

# declare the table.
class ItemTable(Table):
    first = Col('First')
    last = Col('Last')
    city = Col('City')
    name = Col('Name')
    number = Col('Number')

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
    data = cursor.fetchall()
    render_template('table.html', data=data)
    conn.commit()
    conn.close()
    return "Success!"

    # for row in records: 
    #     first = row[0]
    #     last = row[1]
    #     City = row[2]
    #     Name = row[3]
    #     Number = row[4]
    




# # Declare your table
# class ItemTable(Table):
#     name = Col('Name')
#     description = Col('Description')

# # Get some objects
# class Item(object):
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
# items = [Item('Name1', 'Description1'),
#          Item('Name2', 'Description2'),
#          Item('Name3', 'Description3')]
# # Or, equivalently, some dicts
# items = [dict(name='Name1', description='Description1'),
#          dict(name='Name2', description='Description2'),
#          dict(name='Name3', description='Description3')]

# # Or, more likely, load items from your database with something like
# items = ItemModel.query.all()

# # Populate the table
# table = ItemTable(items)

# # Print the html
# print(table.__html__())
# # or just {{ table }} from within a Jinja template