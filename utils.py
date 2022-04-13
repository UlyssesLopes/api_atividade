from models import Pessoas

#insere dados na tabela
def insere_pessoas():
    pessoas = Pessoas(nome='Ulysses', idade=24)
    print(pessoas)

# realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.filter_by.all()
    pessoa = Pessoas.query.filter_by(nome='Ulysses').first()
    print(pessoa.idade)

# altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ulysses').first()
    pessoa.idade = 21
    pessoa.save()

# exclui dados na tabela pessoa
def deleta_pessoas():
    pessoa = Pessoas.query.filter_by(nome='ULysses').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #deleta_pessoas()
    #consulta_pessoas()
    altera_pessoa()
