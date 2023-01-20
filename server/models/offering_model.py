from models.connection_pool import MySQLPool 

class UserModel:
    
    def __init__(self):        
        self.mysql_pool = MySQLPool()
    
    def add_offering(self, price):
        params = {
                'price': price,
        }
        query = 'insert into offering (price) values ( %(price)s)'
        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'price': price}
        return data
    
    def get_offering(self, id_offering):
        params = {'id_offering' : id_offering}
        cursor = self.mysql_pool.execute('select id_offering, price from cliente where id_cliente=%(id_cliente)s', params)
        rv = cursor[0]
        data = {'id_offering': rv[0], 'price': rv[1]}
        return data
    
    def get_all_offering(self):
        cursor = self.mysql_pool.execute('select * from offering')
        data = []
        for rv in cursor:
                content = {'id_offering': rv[0], 'price': rv[1]}
                data.append(content)
        return content
    
    def delete_offering(self, id_offering):
        params = {'id_offering' : id_offering}
        query = 'delete from offering where id_offering = %(id_cliente)s'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result': 1}
        return data