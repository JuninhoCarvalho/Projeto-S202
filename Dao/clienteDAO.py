from bd.database import Graph

class ClienteDAO(object):
    def __init__(self):
        self.db = Graph(uri= 'bolt://18.207.221.149:7687',
                        user='neo4j', password='claps-typists-sail')

    def create(self, cliente):
        return self.db.execute_query('CREATE (c:Cliente {nome:$nome, cpf:$cpf}) return c',
                                     {'nome': cliente['nome'], 'cpf': cliente['cpf']})

    def delete(self, cliente):
        return self.db.execute_query('MATCH (n:Cliente {nome:$nome}) DETACH DELETE n',
                                     {'nome': cliente})