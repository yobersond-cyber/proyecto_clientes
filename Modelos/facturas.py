from pydantic import BaseModel

class facturasbase (BaseModel):
    fecha: str
    val_total: float
    cliente: cliente

class factuacrear (facturasbase):
    pass


class Factura (facturasbase):
    id: int | None = None 