from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from pymongo import MongoClient
from bson import ObjectId  # 👈 Importación necesaria para ObjectId
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configurar MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["PruebaTecnica"]  # Nombre de tu base de datos
products_collection = db["products"]

# Configurar JWT
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

# ================== ENDPOINTS PÚBLICOS ==================
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Validación básica (mejorable con una DB de usuarios)
    if username != "admin" or password != "admin123":
        return jsonify({"error": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# ================== ENDPOINTS PROTEGIDOS ==================
@app.route("/products", methods=["POST"])
@jwt_required()
def add_product():
    data = request.get_json()
    
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Datos incompletos"}), 400

    try:
        price = float(data["price"])  # 👈 Convertir a float
    except ValueError:
        return jsonify({"error": "Precio debe ser numérico"}), 400

    product = {
        "name": data["name"],
        "price": price
    }

    result = products_collection.insert_one(product)
    product["_id"] = str(result.inserted_id)
    
    return jsonify(product), 201

@app.route("/products", methods=["GET"])
@jwt_required()
def list_products():
    products = list(products_collection.find())
    
    for product in products:
        product["_id"] = str(product["_id"])  # Convertir ObjectId a string
    
    return jsonify(products), 200

@app.route("/products/<product_id>", methods=["DELETE"])
@jwt_required()
def delete_product(product_id):
    try:
        obj_id = ObjectId(product_id)  # 👈 Convertir string a ObjectId
    except:
        return jsonify({"error": "ID inválido"}), 400
    
    result = products_collection.delete_one({"_id": obj_id})
    
    if result.deleted_count == 0:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    return jsonify({"message": "Producto eliminado"}), 200

if __name__ == "__main__":
    app.run(debug=True)