class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def __str__(self):
        return f'Cachorro(nome={self.nome}, raca={self.raca}, idade={self.idade})'