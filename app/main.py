from fastapi import FastAPI
from .Enrutadores.clientes import rutas_clientes
from .Enrutadores.facturas import rutas_facturas
from .Enrutadores.transacciones import rutas_transacciones

app = FastAPI()

app.include_router(rutas_clientes, tags=["Clientes"])
app.include_router(rutas_facturas, tags=["Facturas"])
app.include_router(rutas_transacciones, tags=["Transacciones"])