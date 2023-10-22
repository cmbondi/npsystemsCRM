from flask import Flask
from flask import render_template
from classes.db import CRMDatabase

app = Flask(__name__)

@app.route('/')
def Main():
    DB = CRMDatabase()
    clients = DB.get_all_clients()
    # id = clients[0][0]
    # firstname = clients[0][1]
    # lastname = clients[0][2]
    # busname = clients[0][3]
    # status = clients[0][6]
    # date = clients[0][7]
    # return render_template('index.html',
    #     id=id,
    #     firstname=firstname, 
    #     lastname=lastname,
    #     busname=busname,
    #     status = status,
    #     date = date
    #     )
    return render_template('index.html', clients=clients)

@app.route('/detail')
def Detail():
    DB = CRMDatabase()
    client = DB.get_client_byid(1)
    firstname = client[1]
    lastname = client[2]
    busname = client[3]
    phone = client[4]
    email = client[5]
    status = client[6]
    date = client[7]
    info = client[8]
    return render_template('detail.html', 
        firstname=firstname, 
        lastname=lastname,
        busname=busname,
        phone=phone,
        email=email,
        status=status,
        date=date,
        info=info)

@app.route('/add')
def Add():
    return render_template('add.html')

@app.route('/edit')
def Edit():
    return render_template('edit.html')
