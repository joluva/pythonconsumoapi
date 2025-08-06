import requests
import json

def get_data():
    try:
        # creo un diccionario para cargar un producto en fake store
        data={
            "title": "new product",
            "description": "product",
            "price": 12.50,
            "image":"https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_t.png",
            "category": "electronic"
        }
        usuario={
            "username": "johnd",  # Usuario de prueba de la Fake Store API
            "password": "m38rmF$"  # Contraseña de prueba
        }
        
        print(usuario)
        #response = requests.get(' https://pokeapi.co/api/v2/pokemon') # todos los pokemons
        
        # vamos a buscar por habilidades
        #response = requests.get(' https://pokeapi.co/api/v2/ability') # todas las habilidades
        #response = requests.get(' https://pokeapi.co/api/v2/ability/immunity') # una habilidad especifica
        #response = requests.get(' https://pokeapi.co/api/v2/pokemon?limit=20&offset=0') # traigo un limite de pokemons
        #response = requests.get('https://fakestoreapi.com/products') # todos los producto de fake store api
        #response = requests.post('https://fakestoreapi.com/products', data) # uso metodo post para enviar
        response = requests.post('https://fakestoreapi.com/auth/login', usuario) # pedido de login
        
        #print(response.status_code, response.content)
        #print(response.content)
        print(json.dumps(response.json(), indent=2))
        
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
    
if __name__ == "__main__":
    get_data()