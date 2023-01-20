from models.connection_pool import MySQLPool 

class TaskModel:
    
    def __init__(self):        
        self.mysql_pool = MySQLPool()


################### CLiente ################################

    # Funcion para login
    def login_cliente(self,correo,contrasena):
        params = {
            'correo' : correo,
            'contrasena' : contrasena,
        }
        rv = self.mysql_pool.execute("SELECT id_cliente, correo, contrasena from cliente where correo=%(correo)s", params)
        if(len(rv)>0):
            content = {'id_cliente': rv[0][0],'id_correo': rv[0][1],'id_contrasena': rv[0][2],}
            return content
        else:
            return -1


    # Funcion para agregar un cliente
    def add_cliente(self, correo, contrasena,nombre, ape_paterno, ape_materno):
        params = {
            
            'correo' : correo,
            'contrasena' : contrasena,
            'nombre' : nombre,
            'ape_paterno' : ape_paterno,
            'ape_materno' : ape_materno,
        }  
        query = """insert into cliente ( correo, contrasena,nombre,ape_paterno,ape_materno)
            values ( %(correo)s, %(contrasena)s,%(nombre)s,%(ape_paterno)s,%(ape_materno)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_cliente': cursor.lastrowid, 'nombre': nombre, 'correo': correo, 'contrasena': contrasena}
        return data

    # Funcion para obtener un cliente por su ID
    def get_cliente(self, id_cliente):
        params = {'id_cliente' : id_cliente}      
        rv = self.mysql_pool.execute("SELECT id_cliente, nombre, ape_paterno, ape_materno, correo from cliente where id_cliente=%(id_cliente)s", params)
        content = {'id_cliente': rv[0][0], 'nombre': rv[0][1], 'ape_paterno': rv[0][2], 'ape_materno': rv[0][3], 'correo': rv[0][4]}
        return content
    
    # Funcion para obtener todos los clientes
    def get_clientes(self):
        rv = self.mysql_pool.execute("SELECT * from cliente")  
        data = []
        content = {}
        for result in rv:
            content = {'id_cliente': result[0], 'nombre': result[1], 'ape_paterno': result[2], 'correo': result[4]}
            data.append(content)
            content = {}
        return data

    # Funcion para eliminar un cliente
    def delete_cliente(self, id_cliente):
        params = {'id_cliente' : id_cliente}      
        query = """delete from cliente where id_cliente = %(id_cliente)s"""    
        self.mysql_pool.execute(query, params, commit=True)   
        #me parece que no deberia retornar y ser DELETE
        data = {'result': 1}
        return data