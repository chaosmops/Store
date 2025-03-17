# Store
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")

def home():
  return render_template("Store.html")

app.route('/Store.html', methods = ['GET','POST'])



