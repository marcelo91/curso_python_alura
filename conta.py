class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    #Função interna que mostra o saldo
    def extrato(self):
        print(f"Seu saldo atual é de {self.__saldo}")

    #Função interna que ajusta o valor da conta
    def Deposita(self, valor):
        self.__saldo += valor
        # print(f"Seu novo saldo é de {self.__saldo}")

    #Função exclusiva para verificar se existe saldo antes de sacar
    #Função que nao pode ser chamada diretamente
    def __pode_sacar(self,valor):
        saldo_da_conta = self.__saldo + self.__limite
        if valor > saldo_da_conta:
            print(f'Seu limite é de {saldo_da_conta}, amais do que este valor não é permitido')
        else:
            self.__saldo-=valor
    
    #Função que utiliza a função exclusiva da classe atraves do Classe.
    def Sacar(self, valor):
        Conta.__pode_sacar(self,valor)            
        # print(f"Seu novo saldo é de {self.__saldo}")

    #Função que realizar varias outras funções atreladas
    def transfere(self, valor, destino):
        self.Sacar(valor)
        destino.Deposita(valor)

    #Uma propriedade do Objeto e pode ser chamada sem print por exemplo
    @property
    def saldo(self):
        print(self.__saldo)
    
    #Uma propriedade do Objeto e pode ser chamada sem print por exemplo
    @property
    def titular(self):
        return self.__titular
    
    #Uma propriedade do Objeto e pode ser chamada sem print por exemplo
    @property
    def limite(self):
        print(self.__limite)

    #Getters e Setters são usados para pegar e setar dados a um objeto diretamente via função utilizando o = 
    #como se fosse setar novamente somente esse valor especifico
    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    #Metodo estatico que sempre fica da mesma forma
    @staticmethod
    def codigo_banco():
        return '237'



# Extrato
# Deposita
# Saca
# Transfere
