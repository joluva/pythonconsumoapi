import requests
import json
# EL METODO PATCH SIRVE PARA MODIFICAR SOLO ALGUNOS CAMPOS, NO TODOS COMO PUT
def get_data():
    try:        
        data={
            "title": "test product",
            "description": "test",
            "price": 20.50,

        }
        id=input("Ingrese el id del producto a modificar (1-20): ")
        response=requests.patch(f"https://fakestoreapi.com/products/{id}", data) # uso metodo put para enviar
        
        print(json.dumps(response.json(), indent=4))
        
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
    
if __name__ == "__main__":
    get_data()