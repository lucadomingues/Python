class carro:
    def __init__(self, km_litro, tanque_gas=0):
        self.km_litro = km_litro
        self.tanque_gas = tanque_gas

    def andar(self, km):
        print(f'Veículo andou {km}km')
        gasto_combustivel = km / 12
        self.tanque_gas -= gasto_combustivel

    def obter_gasolina(self):
        print(f'Tanque com {self.tanque_gas:.2f}l de combustível')

    def adicionar_gasolina(self):
        litros = float(input('Litros: '))
        self.tanque_gas += litros
        print(f'Abastecimento de {litros:.2f}l')

fusca = carro(12)
fusca.adicionar_gasolina()
fusca.andar(100)
fusca.obter_gasolina()