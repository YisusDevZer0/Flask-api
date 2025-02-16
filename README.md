# flask-products-api
 
# API de Gestión de Productos con Flask y MongoDB

Esta es una API RESTful desarrollada con Flask y MongoDB para gestionar una lista de productos. Incluye autenticación basada en JWT (JSON Web Tokens) y operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para productos.

## Requisitos Previos

- Python 3.8 o superior.
- MongoDB Atlas (o una instancia local de MongoDB).
- Postman (opcional, para probar los endpoints).

## Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/flask-products-api.git
cd flask-products-api
2. Crear un Entorno Virtual
bash
Copy
python -m venv venv
3. Activar el Entorno Virtual
Windows:

bash
Copy
.\venv\Scripts\activate
Linux/Mac:

bash
Copy
source venv/bin/activate
4. Instalar Dependencias
bash
Copy
pip install -r requirements.txt
5. Configurar Variables de Entorno
Crea un archivo .env en la raíz del proyecto con el siguiente contenido:

env
Copy
MONGO_URI=mongodb+srv://usuario:contraseña@cluster0.xxxxx.mongodb.net/nombre_db?retryWrites=true&w=majority
JWT_SECRET_KEY=clave_secreta_compleja_123
MONGO_URI: Cadena de conexión a MongoDB Atlas.

JWT_SECRET_KEY: Clave secreta para firmar los tokens JWT.

6. Ejecutar la Aplicación
bash
Copy
python app.py
La API estará disponible en http://localhost:5000.

