from bd.database import Graph

class VendedorDAO(object):
    def __init__(self):
        self.db = Graph(uri= 'bolt://18.207.221.149:7687',
                        user='neo4j', password='claps-typists-sail')

    def create(self, vendedor):
        return self.db.execute_query('CREATE (c:Vendedor {nome:$nome, cpf:$cpf}) return c',
                                     {'nome': vendedor['nome'], 'cpf': vendedor['cpf']})
