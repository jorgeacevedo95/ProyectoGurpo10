from distutils.log import error
import os
from flask import Flask, jsonify, render_template, flash, request, redirect
import utils

from email.message import EmailMessage
import smtplib
from db import get_db, close_db

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register/')
def register():
    return render_template('register.html')
   
@app.route('/olvidoContraseña/')
def olvidoContraseña():
    return render_template('olvidoContraseña.html')    

@app.route('/administrador/')
def administrador():
    return render_template('administrador.html')

@app.route('/superAdministrador/')
def superAdministrador():
    return render_template('superAdministrador.html')

@app.route('/usuarioFinal/')
def usuarioFinal():
    return render_template('usuarioFinal.html')




































def sql_select_usuarios():
    strql = "SELECT * FROM usuarios"
    con = get_db()
    cursorObj=con.cursor()
    cursorObj.execute(strql)
    usuario = cursorObj.fetchall()
    return usuario

user = get_db.execuite('SELECT USUARIO * FROM WHERE usuario = ?, contraeña '(username, password)).fetchone()
close_db()

if user is None:
    error='Usuario No existe'
else:
    redirect('mensaje')     
flash(error)


    
    
