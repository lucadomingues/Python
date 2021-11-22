def combustivel():
    tipo = int(input('''MENU
    [0] CONFIGURAR
    [1] ETANOL
    [2] GASOLINA
    Digite aqui: '''))
    return tipo

def valor_combustivel(tipo, valor_atualizado=0):
    lista = [1, 5.4, 2, 6.98]
    if valor_atualizado != 0:
        if tipo == 1:
            lista[1] = valor_atualizado
            return lista[1]
        elif tipo == 2:
            lista[3] = valor_atualizado
            return lista[3]
    else:
        if tipo == 1:
            return lista[1]
        elif tipo == 2:
            return lista[3]

def formata_texto(num):
    if num == 1:
        return 'ETANOL'
    elif num == 2:
        return 'GASOLINA'

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro=0, quant_combustivel=100):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quant_combustivel = quant_combustivel

    def abastecer_por_valor(self):
        valor = float(input('Valor R$ '))
        self.valor_litro = valor_combustivel(self.tipo_combustivel)
        litros = valor / self.valor_litro
        print(f'Veículo abastecido com R$ {valor:.2f} de {formata_texto(self.tipo_combustivel)}')
        print(f'Litros abastecido -> {litros:.2f}l')
        self.quant_combustivel -= litros

    def abastecer_por_litro(self):
        litros = float(input('Quantidade de combustível (l) -> '))
        valor = valor_combustivel(self.tipo_combustivel)
        preco_pago = litros * valor
        print(f'Veículo abastecido com {litros:.2f}l de {formata_texto(self.tipo_combustivel)}')
        print(f'Valor a ser pago -> R$ {preco_pago:.2f}')
        self.quant_combustivel -= litros

    def alterar_valor(self):
        tipo_do_combustivel = combustivel()
        valor = float(input('Valor atualizado -> '))
        definir_valor = valor_combustivel(tipo_do_combustivel, valor)
        print(f'Valor de {formata_texto(tipo_do_combustivel)} alterado para R$ {definir_valor:.2f}/l')

    def alterar_combustivel(self):
        self.tipo_combustivel = combustivel()

    def alterar_quant_combustivel(self):
        self.quant_combustivel += float(input(''' - ABASTECER BOMBA
        Quantidade de combustível inserido (l): '''))
        print(f'Bomba com {self.quant_combustivel:.2f}l de combustível')

combus = combustivel()
abastecimento = BombaCombustivel(combus)
abastecimento.alterar_quant_combustivel()