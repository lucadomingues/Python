class ContaInvestimentos:
    def __init__(self, num_conta, correntista, saldo=0, taxa_juros=0):
        self.num_conta = num_conta
        self.correntista = correntista
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    def alterar_nome(self):
        self.correntista = str(input('Nome do correntista: '))
        print(f'Nome alterado para {self.correntista}')

    def deposito(self):
        valor = float(input('Valor do deposito R$: '))
        self.saldo += valor
        print('Depósito realizado com sucesso!')

    def saque(self):
        valor = float(input('Valor de saque R$: '))
        self.saldo -= valor
        print('Saque realizado com sucesso!')

    def adicione_juros(self):
        lucro = self.taxa_juros / 100 * self.saldo
        self.saldo += lucro
        print(f'Lucro de R$ {lucro:.2f}')

    def saldo_atual(self):
        print(f'Saldo atual -> R$ {self.saldo:.2f}')

num = int(input('Número da conta: '))
nome = str(input('Nome do correntista: '))
conta = ContaInvestimentos(num, nome, 0, 10)
conta.alterar_nome()
conta.deposito()
conta.saldo_atual()
conta.saque()
conta.saldo_atual()
conta.adicione_juros()
conta.saldo_atual()