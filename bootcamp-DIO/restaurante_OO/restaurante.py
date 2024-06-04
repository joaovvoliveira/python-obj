class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return (f'{self.nome} | {self.categoria} | {self.ativo}')

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome} | Categoria {restaurante.categoria} | Status: {restaurante.ativo}')

restaurante1 = Restaurante('Jambo', 'Gourmet')
restaurante2 = Restaurante('Hioki', 'Japones')
restaurante3 = Restaurante('Doce Mel', 'Sorveteria')

Restaurante.listar_restaurantes()