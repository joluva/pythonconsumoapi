import requests
import json

def login():
    try:        
        data={
            "username": "johnd",
            "password": "m38rmF$"
        }   
        
        response=requests.post('https://fakestoreapi.com/auth/login', data) # uso metodo post para enviar
        print(json.dumps(response.json(), indent=4))
        
        get_products(response.json()['token']) # Llamo a la funcion get_products y le paso el token
        
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
    
def get_products(token):
    try:        
        headers = {'Authorization': f'Bearer {token}'}
        response=requests.get("https://fakestoreapi.com/products", headers=headers) # uso metodo get para obtener   
        print(json.dumps(response.json(), indent=4))
        
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
        
if __name__ == "__main__":
    login()