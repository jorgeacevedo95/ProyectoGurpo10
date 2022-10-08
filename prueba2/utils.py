

import re
from validate_email import validate_email
import sqlite3
from sqlite3 import Error


pass_reguex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.])[A-Za-z\d@$!%*?&.]{8,}$"
user_reguex = "^[a-zA-Z0-9_.-]+$"
F_ACTIVE = 'ACTIVE'
F_INACTIVE = 'INACTIVE'
EMAIL_APP = 'EMAIL_APP'
REQ_ACTIVATE = 'REQ_ACTIVATE'
REQ_FORGOT = 'REQ_FORGOT'
U_UNCONFIRMED = 'UNCONFIRMED'
U_CONFIRMED = 'CONFIRMED'

def sql_connections():
    try:
        con = sqlite3.connect('EMPLEADOS_IANSA.db')
        return con
    except Error:
        print(Error)

def isEmailValid(email):
	is_valid = validate_email(email)
	return is_valid

def isUsernameValid(user):
	if re.search(user_reguex, user):
		return True
	else:
		return False

def isPasswordValid(password):
	if re.search(pass_reguex, password):
		return True
	else:
		return False

def sql_login_empleados(Correo, Contrasña):
    strsql = "SELECT Categoria FROM Empleados WHERE Correo = '"+Correo+"' AND Contraseña = '"+Contrasña+"';"
    con = sql_connections()
    oCursor = con.cursor()
    oCursor.execute(strsql)
    Cate= oCursor.fetchone()
    con.close()
    return Cate

def sql_select_empleados(Cedula):
    strsql = "SELECT  Nombre, Cargo, Fecha_Ingreso, Fecha_Fin,Tipo_Contrato, Dependencia, Salario, Puntaje FROM Empleados WHERE Cedula = " + Cedula  + ";"
    con = sql_connections()
    oCursor = con.cursor()
    oCursor.execute(strsql)
    Empleado = oCursor.fetchall()
    con.close()
    return Empleado

def sql_edit_empleados(Cedula, Nombre, Cargo, Fecha_Ingreso, Fecha_Fin,Tipo_Contrato, Dependencia, Salario, Puntaje, Correo,Contrasña):
    strsql = "UPDATE Empleados SET Cedula = '" + Cedula + "',  Nombre ='" + Nombre + "', Cargo = '" + Cargo + "', Fecha_Ingreso = " + Fecha_Ingreso + ", Fecha_Fin = " + Fecha_Fin + " , Tipo_Contrato = '" + Tipo_Contrato + "' , Dependencia ='" +  Dependencia + "', Salario = " +  Salario + ", Puntaje = " + Puntaje + ", Correo = '" + Correo+ "', Contrasña = '" + Contrasña +"' WHERE Cedula = " + Cedula + ";"
    con = sql_connections()
    oCursor = con.cursor()
    oCursor.execute(strsql)
    con.commit()
    con.close()
    
    