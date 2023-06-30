from flask import Blueprint, render_template, request, redirect, url_for
import os
from .data import headers, contents, employee_header, table_emp

landingPage = Blueprint('landingPage', __name__)

@landingPage.route('/')
def home():
    return render_template("index.html")

@landingPage.route('/employee/<name>', methods=['GET', 'POST'])
def employee(name):
    content = table_emp("clean")
    content = table_emp(name)
    print(content)
    if request.method == 'POST':
        return render_template("tables.html", headers=headers, contents=contents, tr_class='')
    return render_template("employee.html", headers=employee_header, contents=content, tr_class='')

@landingPage.route('/tables', methods=['GET', 'POST'])
def tables():
    if request.method == 'POST':
        hi = request
        #print("hi\n\n\n", hi, "\n\n")
        howdy = request.form["employee"]
        return redirect(url_for('landingPage.employee', name=howdy)) #f"<h1>{howdy}</h1>"
    else:
        return render_template("tables.html", headers=headers, contents=contents, tr_class='')