from flask import Flask, render_template, redirect, url_for
import os
import time
import threading
import inventory
import vulnerability

app = Flask(__name__, static_folder='static', template_folder='templates')
#Rendering the Home Page
@app.route('/')
def index():
    return render_template('index.html')

#Running the inventry.py script
@app.route('/inventory')
def run_inventory():
    def generate_inventory_report():
        inventory.main()
    threading.Thread(target=generate_inventory_report).start()
    return redirect(url_for('inventory_report'))

#rendering the inventory.html file created via inventory.py
@app.route('/inventory_report')
def inventory_report():
    return render_template('inventory.html')

#running the vulnerablity.py script
@app.route('/vulnerabilities')
def run_vulnerabilities():
    def generate_vulnerability_report():
        vulnerability.main()
    threading.Thread(target=generate_vulnerability_report).start()
    return redirect(url_for('vulnerability_report'))

#Rendering the vulnerablity.html created via vulnerablity.py
@app.route('/vulnerability_report')
def vulnerability_report():
    return render_template('vulnerability.html')

#Rendering Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

#Rendering Recommendation 
@app.route('/recbucket')
def recBucket():
    return render_template('recbucket.html')

if __name__ == '__main__':
    app.run(debug=True)
