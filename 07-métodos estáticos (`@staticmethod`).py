"""
O Organizador (Métodos Estáticos)
"""

"""
Há situações em que uma função pertence à lógica da classe, 
mas não precisa acessar nem o self (instância) nem o cls (classe). Para isso, usamos @staticmethod.
"""

"""
Requisitos:

Crie uma classe Validador.

Crie um método decorado com @staticmethod chamado is_email_valido(email).

Ele deve retornar True se a string do email contiver um "@" e retornar False caso contrário.

O porquê: Funções estáticas são como funções normais, mas ficam "guardadas" dentro da classe para organizar o código.
Você poderá chamá-la direto da classe: Validador.is_email_valido("teste@teste.com").
"""




class Validador:

    @staticmethod
    def email_valido(email: str):
        if "@" in email:
            print("Email valido")
            return True

        else:
            print("Email invalido, revise e tente novamente")
            return False




if __name__ == "__main__":

    validar = Validador()
    get = input("Digite seu email:")
    print(validar.email_valido(get))
