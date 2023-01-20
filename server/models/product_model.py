from models.connection_pool import MySQLPool 

class ProductModel:
    
    def __init__(self):        
        self.mysql_pool = MySQLPool()
        

    def add_product(self, naming, brand, price, details):
        params = {
                'naming': naming,
                'brand': brand,
                'price': price,
                'details': details,
        }
        query = 'insert into product (naming, brand, price, details) values ( %(naming)s, %(brand)s, %(price)s, %(details)s)'
        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'naming': naming, 'brand': brand, 'price': price, 'details': details}
        return data

    # Funcion para obtener un cliente por su ID
    def get_product(self, id_product):
        params = {'id_product' : id_product}
        cursor = self.mysql_pool.execute('select id_product, naming, brand, price, details from cliente where id_cliente=%(id_cliente)s', params)
        rv = cursor[0]
        data = {'id_product': rv[0], 'naming': rv[1], 'brand': rv[2], 'price': rv[3], 'details': rv[4]}
        return data
    
    # Funcion para obtener todos los clientes
    def get_all_product(self):
        cursor = self.mysql_pool.execute('select * from product')
        data = []
        for rv in cursor:
                content = {'id_product': rv[0], 'naming': rv[1], 'brand': rv[2], 'price': rv[3], 'details': rv[4]}
                data.append(content)
        return content

    def delete_product(self, id_product):
        params = {'id_product' : id_product}
        query = 'delete from product where id_product = %(id_cliente)s'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result': 1}
        return data