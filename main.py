from fastapi import FastAPI

app= FastAPI ()
 
#endpoints 

@app.get ("/proyecto")

def mensaje ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar"}


lista_clientes= ["Ricardo","yoberson","quiroga","daniela","ana","kamila","zuelima,"]
@app.get ("/clientes")
def clientes ():
    return {"clientes": lista_clientes} 


