from fastapi import FastAPI, HTTPException
from Modelos.cliente import cliente, clientecrear
app= FastAPI ()

lista_clientes: list [cliente] = []

#endpoints 
@app.get ("/lista de clientes", response_model=list [cliente])
async def listar_clientes ():
    return lista_clientes

#endpoint listar un cliente
@app.get("/clientes/{cliente_id}", response_model=cliente)
async def listar_cliente(cliente_id: int):
    for i, obj_client in enumerate (lista_clientes):
        if obj_client.get("id") == cliente_id:
            return obj_client
        

#endpoint para crear un cliente, y agregarlo a al lista 
@app.post("/crear cliente", response_model=cliente)
async def crear_cliente(datos_cliente: clientecrear):
    cliente_val = cliente.model_validate(datos_cliente.model_dump()) 
    id_cliente = len (lista_clientes) +1 
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val) 
    return cliente_val






