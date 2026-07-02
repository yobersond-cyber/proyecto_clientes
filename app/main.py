from fastapi import FastAPI, HTTPException, status
from .Modelos.cliente import cliente, clientecrear, clienteeditar
from .Modelos.facturas import Factura, facturacrear, facturaeditar
from .Modelos.transacciones import Transaccion, transaccioncrear, transaccioneditar


app= FastAPI ()

lista_clientes: list [cliente] = []
lista_facturas: list [Factura] = []
lista_transacciones: list [Transaccion] = []  

#endpoints 
@app.get ("/lista de clientes", response_model=list [cliente])
async def listar_clientes ():
    return lista_clientes

#endpoint listar un cliente
@app.get("/clientes/{cliente_id}", response_model=cliente)
async def listar_cliente(cliente_id: int):
    for i, obj_client in enumerate (lista_clientes):
        if obj_client.id == cliente_id:
            return obj_client
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )
        

#endpoint para crear un cliente, y agregarlo a al lista 
@app.post("/crear cliente", response_model=cliente)
async def crear_cliente(datos_cliente: clientecrear):
    cliente_val = cliente.model_validate(datos_cliente.model_dump()) 
    id_cliente = len (lista_clientes) +1 
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val) 
    return cliente_val


@app.patch("/clientes/{cliente_id}", response_model=cliente)
async def editar_cliente(cliente_id: int, datos_cliente: clienteeditar):
    for i, obj_cliente in enumerate(lista_clientes):
        for i, obj_client in enumerate (lista_clientes):
            if obj_client.id == cliente_id:
                cliente_val = cliente.model_validate(datos_cliente.model_dump())
                cliente_val.id = cliente_id
                lista_clientes [i] = cliente_val 
                return cliente_val
    raise HTTPException (
        status_code=400,detail=f"el cliente con id {cliente_id}, no existe."
        )

# endpoint eliminar cliente
@app.delete("/clientes/{cliente_id}", response_model=cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe."
    )



#endpoints para facturas 

@app.get ("/facturas", response_model=list [Factura])
async def listar_facturas ():
    return lista_facturas


@app.get ("/facturas/{cliente_id}", response_model= Factura)
async def listar_facturas (factura_id: int):
    for i, obj_factura in enumerate (lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe."
    )


@app.post ("/facturas/{cliente_id}", response_model= Factura)
async def crear_factura (cliente_id: int, datos_factura: facturacrear):
    #buscar el cliente
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado =  cliente 
        
        if not cliente_encontrado:
          raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"el cliente con id {cliente_id}, no existe."
        )  


        #validar datos de la factura
        factura_val = Factura.model_validate(datos_factura.model_dump())
        factura_val.cliente = cliente_encontrado
        #id de la factura
        factura_val.id = len (lista_facturas) +1  
        lista_facturas.append (factura_val)
        return factura_val






@app.patch ("/facturas/{factura_id}", response_model= Factura)
async def editar_factura (factura_id: int, datos_factura: Factura):
    pass

@app.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura (factura_id):
    pass

#endpoint para transacciones 


@app.get ("/transacciones", response_model=list [Transaccion])
async def listar_transacciones ():
    return lista_transacciones


@app.get ("/transacciones/{transacciones_id}", response_model= Transaccion)
async def listar_transacciones (id_transacciones: int):
    pass

@app.post ("/transacciones/{factura_id}", response_model= Transaccion)
async def crear_transacciones (factura_id: int, datos_transacciones: transaccioncrear):
    #buscar una factura
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == factura_id:  
            factura_encontrada =  factura 
        
        if not factura_encontrada:
          raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe."
        )  

        #validar datos de la transaccion
        transaccion_val = Transaccion.model_validate(datos_transacciones.model_dump())
        transaccion_val.factura_id = factura_id
        factura_encontrada.transacciones.append(transaccion_val)
        #id de la transaccion
        transaccion_val.id  = len (lista_transacciones) + 1     
        lista_transacciones.append (transaccion_val)
        return transaccion_val

@app.patch ("/transacciones/{transacciones_id}", response_model= Transaccion)
async def editar_transacciones (id_transacciones: int, datos_transacciones: Transaccion):
    pass

@app.delete("/transacciones/{transacciones_id}", response_model= Transaccion)
async def eliminar_transaccion (transacciones_id):
    pass
