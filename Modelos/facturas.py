from pydantic import BaseModel

class facturasbase (BaseModel):
    fecha: str
    val_total: float