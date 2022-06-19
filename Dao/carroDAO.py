from bd.database import Graph

class CarroDAO(object):
    def __init__(self):
        self.db = Graph(uri= 'bolt://18.207.221.149:7687',
                        user='neo4j', password='claps-typists-sail')

    def create(self, carro):
        return self.db.execute_query('CREATE (c:Carro {marca:$marca, modelo:$modelo, cor:$cor, ano:$ano}) return c',
                                     {'marca': carro['marca'], 'modelo': carro['modelo'], 'cor': carro['cor'], 'ano': carro['ano']})

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n:Carro) RETURN n')

    def update_cor(self, carro):
        return self.db.execute_query('MATCH (n:Carro {modelo:$modelo}) SET n.cor = $cor RETURN n',
                                     {'modelo': carro['modelo'], 'cor': carro['cor']})
