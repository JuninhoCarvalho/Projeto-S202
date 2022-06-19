import pessoa

class Vendedor(pessoa.Pessoa):
    def __init__(self, nome, cpf, dataVenda):
        super().__init__(nome, cpf)
    
    def compraCarro():
        print("Vendeu um carro")