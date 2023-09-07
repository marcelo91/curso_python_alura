class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        

    def extrato(self):
        print(f"Seu saldo atual é de {self.__saldo}")

    def Deposita(self, valor):
        self.__saldo += valor
        # print(f"Seu novo saldo é de {self.__saldo}")

    def __pode_sacar(self,valor):
        saldo_da_conta = self.__saldo + self.__limite
        if valor > saldo_da_conta:
            print(f'Seu limite é de {saldo_da_conta}, amais do que este valor não é permitido')
        else:
            self.__saldo-=valor

    def Sacar(self, valor):
        Conta.__pode_sacar(self,valor)            
        # print(f"Seu novo saldo é de {self.__saldo}")

    def transfere(self, valor, destino):
        self.Sacar(valor)
        destino.Deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return '237'



# Extrato
# Deposita
# Saca
# Transfere
