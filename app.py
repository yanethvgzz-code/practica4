from flask import Flask, redner_templete, request, jsonify, make_response, session 
app = Flask(__name__)

@app.route('/detalle_pedido')
def detalle_pedido():
    import mysql.connector
mydb = mysql.connector.connect(
  host="46.28.42.226",
  user="u760464709_24005242_usr",
  password="u7?Jpkt>Y*E7",
  database="u760464709_24005242_bd"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM detalle_pedido")
myresult = mycursor.
return male_repose(jsonify(myresult))

mycursor = mydb.cursor()

sql = "INSERT INTO detalle_pedido (id_detalle, id_pedido, id_producto, cantidad, precio_unitario)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()
