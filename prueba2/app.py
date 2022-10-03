import email
import os
from flask import Flask, render_template, flash
import utils

from email.message import EmailMessage
import smtplib


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





