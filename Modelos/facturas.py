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
        # valor total factura (cantidad * valos unit)
        # consultar el id actual de la factura 
        factura_id_actual = getattr(self, "id", None)
        total_factura = 0.0
        if not factura_id_actual or not self.transacciones:
            return total_factura
        #recorrer la lista de trasacciones con el id de factrura
        for transacciones in self.transacciones:
            if Transaccion.factura_id == factura_id_actual:
                total_factura += Transaccion.val_unitario * Transaccion.cantidad
        return total_factura


class facturacrear (facturasbase):
    pass

class facturaeditar (facturasbase):
    pass


class Factura (facturasbase):
    id: int | None = None 

