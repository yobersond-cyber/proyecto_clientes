from fastapi import APIRouter, HTTPException, status
from ..Modelos.facturas import Factura
from ..Modelos.transacciones import Transaccion, transaccioncrear

rutas_transacciones = APIRouter()

lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

@rutas_transacciones.get("/transacciones/{transacciones_id}", response_model=Transaccion)
async def listar_transaccion(transacciones_id: int):
    for obj_transaccion in lista_transacciones:
        if obj_transaccion.id == transacciones_id:
            return obj_transaccion
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La transacción con id {transacciones_id}, no existe."
    )

@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transacciones(factura_id: int, datos_transacciones: transaccioncrear):
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura
            break

    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )

    transaccion_val = Transaccion.model_validate(datos_transacciones.model_dump())
    transaccion_val.factura_id = factura_id
    transaccion_val.id = len(lista_transacciones) + 1
    lista_transacciones.append(transaccion_val)
    return transaccion_val

@rutas_transacciones.patch("/transacciones/{transacciones_id}", response_model=Transaccion)
async def editar_transacciones(transacciones_id: int, datos_transacciones: Transaccion):
    pass

@rutas_transacciones.delete("/transacciones/{transacciones_id}", response_model=Transaccion)
async def eliminar_transaccion(transacciones_id: int):
    pass
