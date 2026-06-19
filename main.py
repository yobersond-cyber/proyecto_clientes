from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI ()
 
#endpoints 

@app.get ("/proyecto")

def mensaje ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar"}


lista_clientes= ["Ricardo","yoberson","quiroga","daniela","ana","kamila","zuelima,"]
@app.get ("/clientes")
def clientes ():
    return {"clientes": lista_clientes} 



app = FastAPI()

class Cliente(BaseModel):
    id: int
    nombre: str
    correo: str
    descripcion: str

class Factura(BaseModel):
    id: int
    fecha: str
    Valortotal: float
    cliente_id: int

class Transaccion(BaseModel):
    id: int
    metodo_pago: str
    monto: float
    factura_id: int


