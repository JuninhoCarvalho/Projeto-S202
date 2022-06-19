from pprint import pprint as pp
from gridfs import Database
from Dao.carroDAO import CarroDAO
from Dao.clienteDAO import ClienteDAO
from Dao.vendedorDAO import VendedorDAO
from Dao.comprarCarroDAO import ComprarCarroDAO
from bd.database import Graph
from datetime import date

def divider():
    print('\n' + '-' * 80 + '\n')

carroDao = CarroDAO()
clienteDao = ClienteDAO()
vendedorDao = VendedorDAO()
comprarCarroDao = ComprarCarroDAO()

while 1:    
    option = input('1. Cadastrar carro\n2. Cadastrar Cliente\n3. Cadastrar Vendedor\n4. Atualizar cor do carro' + 
    '\n5. Mostrar carros disponíveis\n6. Comprar carro\n7. Deletar cliente\n8. Sair\n')

    if option == '1':
        marca = input('  Marca: ')
        modelo = input('  Modelo: ')
        cor = input('  Cor: ')
        ano = input('  Ano: ')
        carro = {
            'marca': marca,
            'modelo': modelo,
            'cor': cor,
            'ano': ano
        }
        aux = carroDao.create(carro)
        divider()

    elif option == '2':
        nome = input('Nome: ')
        cpf = input(' Cpf: ')
        cliente = {
            'nome': nome,
            'cpf': cpf
        }
        aux = clienteDao.create(cliente)
        divider()

    elif option == '3':
        nome = input('Nome: ')
        cpf = input(' Cpf: ')
        vendedor = {
            'nome': nome,
            'cpf': cpf
        }
        aux = vendedorDao.create(vendedor)
        divider()
    
    elif option == '4':
        modelo = input('  Modelo: ')
        cor = input('  Cor: ')
        carro = {
            'modelo': modelo,
            'cor': cor
        }
        aux = carroDao.update_cor(carro)
        divider()

    elif option == '5':
        aux = carroDao.read_all_nodes()
        pp(aux)
        divider()

    elif option == '6':
        nomeCliente = input('  Nome Cliente: ')
        nomeVendedor = input('  Nome Vendedor: ')
        data = date.today()
        modelo = input('  Modelo: ')
        marca = input('  Marca: ')
        carro = {
            'modelo': modelo,
            'marca': marca
        }
        comprarCarroDao.create_relation(nomeCliente, carro, nomeVendedor, data)
        divider()

    elif option == '7':
        nome = input(' Nome: ')
        aux = clienteDao.delete(nome)
        pp(aux)
        divider()

    elif option == '8':
        break

    else:
        print("Entre com uma opção válida!")

carroDao.db.close()
clienteDao.db.close()
vendedorDao.db.close()
comprarCarroDao.db.close()