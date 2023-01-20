from models.connection_pool import MySQLPool 

class UserModel:
    
    def __init__(self):        
        self.mysql_pool = MySQLPool()
        

    def add_user(self, given_name, family_name, email):
        params = {
                'given_name': given_name,
                'family_name': family_name,
                'email': email,
        }
        query = 'insert into user (given_name, family_name, email) values ( %(given_name)s, %(family_name)s, %(email)s)'
        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'given_name': given_name, 'family_name': family_name, 'email': email}
        return data

    def get_user(self, id_user):
        params = {'id_user' : id_user}
        cursor = self.mysql_pool.execute('select id_user, given_name, family_name, email from cliente where id_cliente=%(id_cliente)s', params)
        rv = cursor[0]
        data = {'id_user': rv[0], 'given_name': rv[1], 'family_name': rv[2], 'email': rv[3]}
        return data
    

    def get_all_user(self):
        cursor = self.mysql_pool.execute('select * from user')
        data = []
        for rv in cursor:
                content = {'id_user': rv[0], 'given_name': rv[1], 'family_name': rv[2], 'email': rv[3]}
                data.append(content)
        return content


    def delete_user(self, id_user):
        params = {'id_user' : id_user}
        query = 'delete from user where id_user = %(id_cliente)s'
        self.mysql_pool.execute(query, params, commit=True)
        data = {'result': 1}
        return data