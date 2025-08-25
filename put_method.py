import requests
import json

def get_data():
    try:        
        data={
            "title": "test product",
            "description": "test",
            "price": 20.50,
            "image":"https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_t.png",
            "category": "electronic"
        }
        id=input("Ingrese el id del producto a modificar (1-20): ")
        response=requests.put(f"https://fakestoreapi.com/products/{id}", data) # uso metodo put para enviar
        
        print(json.dumps(response.json(), indent=4))
        
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
    
if __name__ == "__main__":
    get_data()