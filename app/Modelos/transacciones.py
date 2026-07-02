from pydantic import BaseModel

class transaccionbase (BaseModel):
    cantidad: int 
    val_unitario: float
    
    

class transaccioncrear(transaccionbase):
    pass

class transaccioneditar (transaccionbase):
    pass

class Transaccion (transaccionbase):
    id: int | None = None
    factura_id: int | None = None 
    #aqui va la relacion con el modelo factura (solo un campo)