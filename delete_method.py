import requests
import json
# EL METODO PATCH SIRVE PARA MODIFICAR SOLO ALGUNOS CAMPOS, NO TODOS COMO PUT6
def get_data():
    try:        
        id=input("Ingrese el id del producto a eliminar (1-20): ")
        response=requests.delete(f"https://fakestoreapi.com/products/{id}") # uso metodo delete para eliminar
        
        print(json.dumps(response.json(), indent=4))
        print("Producto eliminado")
    except requests.exceptions.RequestException as err:
        print(f"Ha ocurrido un error: {err}")
    
if __name__ == "__main__":
    get_data()