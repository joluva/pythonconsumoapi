import requests
import json

def get_data():
    try:       
        # armamos un diccionario con los headers
        data={"title": "test product", "price": 10} 
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        #response=requests.get("https://fakestoreapi.com/carts/6", headers=headers) # uso metodo get para obtener   
        response=requests.post("https://fakestoreapi.com/products/", headers=headers, json=data) # uso metodo get para obtener
        # si no se pone json=data, no toma los headers
        print(json.dumps(response.json(), indent=4))
        
        # El siguiente codigo es para ver los headers que devuelve la peticion
        print("\nHeaders de la peticion")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
    
if __name__ == "__main__":
    get_data()