# Criando classe Veiculo

class Veiculo:

# Criando método contrutor
    def __init__(self,marca,modelo,cor,):

        self.marca = marca
        self.modelo = modelo
        self.cor = cor          # ATRIBUTOS
        self.velocidade = 0
        self.motor: bool = False


    # Métodos
    # Dá partida no veiculo
    # Antes  de dá a partida o método verifica se o carro já esta ligado
    def partida(self):

       if not self.motor:
            self.motor = True
            print('O MOTOR ESTA LIGADO')

       else:
           print('O MOTOR JÁ ESTA FUNCIONADO')

    # Desliga o carro
    # Verifica se o carro esta realmente ligado antes de desligar
    def desligar_motor(self):

        if self.motor:
            self.motor = False
            print('O MOTOR ESTA DESLIGADO')

        else:
            print('O MOTOR JÁ ESTA DESLIGADO')


    # Aumenta a velocidade do veiculo.
    # Verifica se está ligado antes de acelerar
    def acelerar(self):
        if self.motor:
            self.velocidade += 5
            print(f'ACELERANDO VELOCIDADE ATUAL: {self.velocidade}')

        else:
            print('O  MOTOR ESTA DESLIGADO')

    # Freia o carro
    # Verifica se o carro está ligado e se não está parado antes de freiar
    def freiar(self):

        if self.motor:

            if self.velocidade > 0:
                self.velocidade -= 5
                print(f'FREIAR VELOCIDADE: {self.velocidade}')

            else:
                print(f'O MOTOR ESTA PARADO VELOCIDADE: {self.velocidade}')

        else:
            print('O  MOTOR ESTA DESLIGADO')

    # Método que mostra as especificações do veiculo
    def mostrar_especificacoes(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}')


# Criando objeto carro1



'''carro1 = Veiculo('Ford', 'Mustang', 'Vermelho')

carro1.partida()

carro1.mostrar_especificações()

carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()

carro1.freiar()'''

#carro1.desligar_motor()

# Verificando se o metodo reage se tentar desligar o carro duas vezes
#carro1.desligar_motor()

# Mesmo caso só que com a partida
#carro1.partida()

# Criando class filha moto

class moto(Veiculo): # Com o método contrutor herdando atributos da class pai

    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo, cor)
        self.grau: bool = False



    def grau180(self): # O nome do método não pode ser o mesmo do atribuuto
        if self.motor:
            self.grau = True
            print('PUXANDO GRAU')


        else:
            print('O MOTOR ESTA DESLIGADO, DE PARTIDA ANTES DE PUXAR O GRAU')


# Criando objeto moto1 com a classe filha moto herdada da classe pai Veiculo
moto1 = moto('Honda', 'Bros', 'Branco')

moto1.partida()

moto1.mostrar_especificações()

moto1.acelerar()
moto1.acelerar()
moto1.acelerar()

moto1.grau180()

moto1.freiar()

#moto1.desligar_motor()
#moto1.grau180()







