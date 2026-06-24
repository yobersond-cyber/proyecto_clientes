from pydantic import BaseModel
class Clientebase(BaseModel):
    nombre: str
    email: str
    descripcion: str

class clientecrear (Clientebase):
    pass

class cliente (Clientebase):
    id: int | None = None 