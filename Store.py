# Store
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")

def home():
  return render_template("store.html")

app.route('/cupcake.html', methods = ['GET','POST'])
def add_cupcake():
  
    if request.method == 'POST': 

        title = request.form['name'] 

        price = request.form['preis'] 

        toppings = request.form['garnierungen'] 

        type = request.form['sorte']

        print(title)
        print(price)
        print(toppings)
        print(type)


        conn = sqlite3.connect('cupcakes.db') 

        cursor = conn.cursor()  

        cursor.execute(f"INSERT INTO cupcakes (name, preis, garnierungen, sorte) VALUES ('{title}', '{price}', '{toppings}','{type}')") 

         

        conn.commit()  

        conn.close() 
  

        print(f"Titel: {title}, Preis: {price}, Garnierungen: {toppings}, Sorte: {type}") 

         

        return "Die Daten wurden erfolgreich übermittelt!" 
    
    return render_template("cupcake.html")

if __name__ == '__main__':  

    app.run(debug=True)  



