from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/process', methods=['POST'])
def send_message():
    data = {
        "message" : request.form["message"],
        "message_id": request.form["message_id"]
    }
    print(request.form)
    id = Message.save(data)
    return redirect('/dashboard')
    

@app.route('/delete')
def delete_message(id):
    data = {
        'id' : id
    }
    Message.destroy(data)
    return redirect('/dashboard')