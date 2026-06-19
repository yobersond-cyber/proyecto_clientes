from fastapi import FastAPI

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


lista_clientes = [
    {"id": 1, "nombre": "Lady", "email": "lady@gmail.com", "edad": 22, "descripcion": "NA"},
    {"id": 2, "nombre": "Luis", "email": "luis@gmail.com", "edad": 19, "descripcion": "NA"},
    {"id": 3, "nombre": "Ana", "email": "ana@gmail.com", "edad": 23, "descripcion": "Cliente frecuente"},
    {"id": 4, "nombre": "Carlos", "email": "carlos@gmail.com", "edad": 25, "descripcion": "Cliente nuevo"},
    {"id": 5, "nombre": "Sofía", "email": "sofia@gmail.com", "edad": 21, "descripcion": "NA"},
    {"id": 6, "nombre": "Andrés", "email": "andres@gmail.com", "edad": 28, "descripcion": "Cliente activo"}
 ]

#endpoints 
@app.get ("/")
def listar_clientes ():
    return lista_clientes




