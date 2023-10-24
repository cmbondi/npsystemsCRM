from flask import Flask, render_template, request, redirect
from classes.db import CRMDatabase

app = Flask(__name__)

@app.route('/')
def Main():
    DB = CRMDatabase()
    clients = DB.get_all_clients()
    DB.db_close()
    return render_template('index.html', clients=clients)

@app.route('/detail/<int:id>')
def Detail(id):
    DB = CRMDatabase()
    client = DB.get_client_byid(id)
    DB.db_close()
    firstname = client[1]
    lastname = client[2]
    busname = client[3]
    phone = client[4]
    email = client[5]
    status = client[6]
    date = client[7]
    info = client[8]
    return render_template('detail.html', 
        id=id,
        firstname=firstname, 
        lastname=lastname,
        busname=busname,
        phone=phone,
        email=email,
        status=status,
        date=date,
        info=info)

@app.route('/add', methods=['GET', 'POST'])
def Add():
    if request.method == "POST":
        DB = CRMDatabase()
        DB.add_client(
            request.form["firstname"], 
            request.form["lastname"], 
            request.form["busname"],
            request.form["phone"],
            request.form["email"],
            request.form["status"],
            request.form["date"],
            request.form["info"]
            )
        DB.db_close()
        return redirect('/')
    else:
        return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def Edit(id):
    DB = CRMDatabase()
    if request.method == "GET":
        client = DB.get_client_byid(id)
        return render_template('edit.html', client=client)
    elif request.method == "POST":
        DB.edit_client(
            id,
            request.form["firstname"], 
            request.form["lastname"], 
            request.form["busname"],
            request.form["phone"],
            request.form["email"],
            request.form["status"],
            request.form["date"],
            request.form["info"]
            )
        DB.db_close()
        return redirect('/')

@app.route('/delete/<int:id>')
def Delete(id):
    DB = CRMDatabase()
    DB.delete_client(id)
    DB.db_close()
    return redirect('/')
