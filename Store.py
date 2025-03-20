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

        print(name)
        print(price)
        print(toppings)


        conn = sqlite3.connect('cupcakes.db') 

        cursor = conn.cursor()  

        cursor.execute(f"INSERT INTO cupcakes (name, price, toppings) VALUES ('{name}', '{preis}', '{garnierungen}')") 

         

        conn.commit()  

        conn.close() 
  

        print(f"Titel: {title}, Preis: {price}, Garnierungen: {toppings}") 

         

        return "Die Daten wurden erfolgreich übermittelt!" 
    
    return render_template("cupcake.html")

if __name__ == '__main__':  

    app.run(debug=True)  



