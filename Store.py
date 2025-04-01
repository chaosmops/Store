# Store
import sqlite3
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
@app.route("/")

def home():
  return render_template("store.html")

@app.route('/cupcake.html', methods = ['GET','POST'])
def add_cupcake():
  
    if request.method == 'POST': 

        title = request.form['name'] 

        toppings = request.form['garnierungen'] 

        type = request.form['sorte']

        toppingprice = request.form['garnierungspreis'] 

        typeprice = request.form['sortenpreis'] 

        print(title)
        print(toppings)
        print(type)
        print(toppingprice)
        print(typeprice)



        conn = sqlite3.connect('cupcakes.db') 

        cursor = conn.cursor()  

        cursor.execute("""
            "CREATE TABLE" cupcake (
                       
                name INTEGER PRIMARY KEY TEXT NOT NULL,
                       
                garnierungen TEXT NOT NULL,
                       
                sorte TEXT NOT NULL,
                       
                garnierungspreis NOT NULL NUMERIC,
                       
                sortenpreis NOT NULL NUMERIC)
                    
            """)

        cursor.execute(f"INSERT INTO cupcakes (name, garnierungen , sorte, garnierungspreis , sortenpreis) VALUES ('{title}', '{toppings}', '{type}', '{toppingprice}', '{typeprice}')") 

         

        conn.commit()  

        conn.close() 
  

        print(f"Titel: {title}, Garnierungen: {toppings}, Sorte: {type}, Garnierungspreis: {toppingprice}, Sortenpreis: {typeprice}") 

         

        return "Die Daten wurden erfolgreich übermittelt!" 
    
    return render_template("cupcake.html")

if __name__ == '__main__':  

    app.run(debug=True)  


#app.route('/register.html', methods = ['GET','POST'])
#def add_rigster():

    #if request.method == 'POST': 










