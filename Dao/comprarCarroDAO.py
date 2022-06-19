from venv import create
from bd.database import Graph

class ComprarCarroDAO(object):
    def __init__(self):
        self.db = Graph(uri= 'bolt://18.207.221.149:7687',
                        user='neo4j', password='claps-typists-sail')

    def create_relation(self, cliente, carro, vendedor, data):
        self.db.execute_query('MATCH (n:Cliente {nome:$nome}), (m:Vendedor {nome:$nome1}) CREATE (n)-[r:ComprouDe{dataCompra: $data, marca:$marca, modelo:$modelo}]->(m) RETURN n, r, m',
                                     {'nome': cliente, 'nome1': vendedor, 'data': data, 'marca': carro['marca'], 'modelo': carro['modelo']})

        self.db.execute_query('MATCH (n:Cliente {nome:$nome}), (m:Carro {modelo:$modelo}) CREATE (n)-[r:Possui{dataCompra: $data}]->(m) RETURN n, r, m',
                                     {'nome': cliente, 'data': data, 'modelo': carro['modelo']})

        self.db.execute_query('MATCH (n:Carro {modelo:$modelo}) SET n.vendido = true ', {'modelo': carro['modelo']})