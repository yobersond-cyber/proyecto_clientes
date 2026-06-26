from pydantic import BaseModel, computed_field
from .transacciones import Transaccion
from .cliente import cliente
from datetime import datetime

class facturasbase (BaseModel):
    fecha: str = datetime.now ()
    cliente: cliente
    transacciones: list [Transaccion] = []

    @computed_field
    @property
    def val_total(self) -> float:
        return 222

class facturacrear (facturasbase):
    pass

class facturaeditar (facturasbase):
    pass


class Factura (facturasbase):
    id: int | None = None 

