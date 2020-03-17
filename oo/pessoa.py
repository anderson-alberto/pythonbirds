class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    alberto = Pessoa(nome="Alberto ")
    anderson = Pessoa(alberto, nome = "Anderson")
    print(Pessoa.cumprimentar(anderson))
    print(id(anderson))
    print(anderson.cumprimentar())
    print (anderson.nome)
    print(anderson.idade)
    for filho in anderson.filhos:
        print(filho.nome)
    anderson.sobrenome = "Correa"
    del anderson.filhos
    alberto.olhos = 1
    del alberto.olhos
    print(anderson.__dict__)
    print(alberto.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(anderson.olhos)
    print(alberto.olhos)
    print(id(Pessoa.olhos), id(anderson.olhos), id(alberto.olhos))