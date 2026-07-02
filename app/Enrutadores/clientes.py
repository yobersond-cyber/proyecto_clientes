from fastapi import APIRouter, HTTPException
from ..Modelos.cliente import cliente, clientecrear, clienteeditar
from ..Modelos.facturas import Factura
from ..Modelos.transacciones import Transaccion

rutas_clientes = APIRouter()

lista_clientes: list[cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

@rutas_clientes.get("/clientes", response_model=list[cliente])
async def listar_clientes():
    return lista_clientes

# endpoint listar un cliente
@rutas_clientes.get("/clientes/{cliente_id}", response_model=cliente)
async def listar_cliente(cliente_id: int):
    for obj_client in lista_clientes:
        if obj_client.id == cliente_id:
            return obj_client
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )

# endpoint para crear un cliente y agregarlo a la lista
@rutas_clientes.post("/clientes", response_model=cliente)
async def crear_cliente(datos_cliente: clientecrear):
    cliente_val = cliente.model_validate(datos_cliente.model_dump())
    id_cliente = len(lista_clientes) + 1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

@rutas_clientes.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente: clienteeditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_actualizado = obj_cliente.model_copy(update=datos_cliente.model_dump(exclude_unset=True))
            lista_clientes[i] = cliente_actualizado
            return cliente_actualizado

    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )

# endpoint eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )