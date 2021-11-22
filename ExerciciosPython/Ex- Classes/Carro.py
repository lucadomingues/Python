class Carro:
    def __init__(self, modelo, cor, cambio, andando=False, parado=True, estacionando=False):
        self.modelo = modelo
        self.cor = cor
        self.cambio = cambio
        self.andando = andando
        self.parado = parado
        self.estacionando = estacionando

    def andar(self):
        if self.andando:
            print(f'Carro já está andando.')
        else:
            print('Carro começou a andar.')
            self.andando=True
            self.parado = False
            self.estacionando=False

    def parar(self):
        if self.parado:
            print('Carro já está parado.')
        else:
            print('Carro está parando.')
            self.parado=True
            self.andando=False

    def estacionar(self):
        if self.estacionando:
            print('Carro ja está estacionado')
        else:
            if self.parado:
                print('Carro estacionando')
                self.estacionando=True
                self.andando=False
            else:
                print('Veículo precisa parar para estacionar')

carro1 = Carro('Sedan', 'Prata', 'Manual')
carro1.andar()
carro1.andar()
carro1.parar()
carro1.parar()
carro1.estacionar()
carro1.estacionar()
carro1.andar()
carro1.estacionar()