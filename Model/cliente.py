import pessoa

class Cliente(pessoa.Pessoa):
    def __init__(self, nome, cpf, dataCompra):
        super().__init__(nome, cpf)
    
    def compraCarro():
        print("comprou um carro")