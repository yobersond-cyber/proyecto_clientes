from pydantic import BaseModel
from cliente import cliente

class facturasbase (BaseModel):
    fecha: str
    val_total: float
    cliente: cliente

class factuacrear (facturasbase):
    pass

class facturaeditar (facturasbase):
    pass


class Factura (facturasbase):
    id: int | None = None 