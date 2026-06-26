from pydantic import BaseModel

class transaccionbase (BaseModel):
    cantidad: int 
    val_unitario: float
    factura_id: int 

class transaccioncrear(transaccionbase):
    pass

class transaccioneditar (transaccionbase):
    pass

class Transaccion (transaccionbase):
    id: int | None = None 