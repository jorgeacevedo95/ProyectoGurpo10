import os
from flask import Flask, jsonify, render_template, flash, request, redirect, url_for
import utils
from utils import *

from email.message import EmailMessage
import smtplib
from db import get_db, close_db

app=Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usua = request.form['usuario']
        contra = request.form['password']
        categoria = sql_login_empleados(usua, contra)
        if categoria == None:
            return render_template('login.html')
        elif categoria[0] == 0:
            return redirect(url_for('superAdministrador'))
        elif categoria[0] == 1:
            return render_template('administrador.html')
        elif categoria[0] == 2:
            return render_template('usuariofinal.html')
    else:
        return render_template('login.html')

@app.route('/register/')
def register():
    return render_template('register.html')
   
@app.route('/olvidoContraseña/')
def olvidoContraseña():
    return render_template('olvidoContraseña.html')    

@app.route('/superAdministrador/', methods=['GET','POST'])
def superAdministrador():
    if request.method == 'POST':
        id = request.form['BuscarEmpleadoGestionarSA']
        emple = sql_select_empleados(id)
        print(emple)
        
        
        return render_template('superAdministrador.html')
    else:
        return render_template('superAdministrador.html')

@app.route('/administrador/')
def administrador():
    return render_template('administrador.html')

@app.route('/usuarioFinal/')
def usuarioFinal():
    return render_template('usuarioFinal.html')
















