from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI ()

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str


class Factura(BaseModel):
    id: int
    cliente_id: int
    vrtotal: float





class Transaccion(BaseModel):
    id: int
    vr_unitario: float
    cantidad: int
    factura_id: int


lista_clientes: list [Cliente] = [
    {"id": 1, "nombre": "Lady", "email": "lady@gmail.com", "edad": 22, "descripcion": "NA"},
    {"id": 2, "nombre": "Luis", "email": "luis@gmail.com", "edad": 19, "descripcion": "NA"},
    {"id": 3, "nombre": "Ana", "email": "ana@gmail.com", "edad": 23, "descripcion": "Cliente frecuente"},
    {"id": 4, "nombre": "Carlos", "email": "carlos@gmail.com", "edad": 25, "descripcion": "Cliente nuevo"},
    {"id": 5, "nombre": "Sofía", "email": "sofia@gmail.com", "edad": 21, "descripcion": "NA"},
    {"id": 6, "nombre": "Andrés", "email": "andres@gmail.com", "edad": 28, "descripcion": "Cliente activo"}
 ]

#endpoints 
@app.get ("/lista de clientes", response_model=list [Cliente])
def listar_clientes ():
    return lista_clientes

#endpoint listar un cliente
@app.get("/clientes/{cliente_id}", response_model=Cliente)
def listar_cliente(cliente_id: int):
    for i, obj_client in enumerate (lista_clientes):
        if obj_client.get("id") == cliente_id:
            return obj_client
        

#endpoint para crear un cliente, y agregarlo a al lista 
@app.post("/crear cliente", response_model=Cliente)
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente) 
    return datos_cliente 






