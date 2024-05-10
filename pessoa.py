class Pessoa: #substantivo
    #
    def __init__(self, nome: str, idade: int, cpf) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):#verbos -> métodos
        print('Estou correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
            print('Estou bebendo cerveja')

    def __apresentar_documento(self):
        print(self.__cpf)

    def __apresentar_documento(self):
        print(self.__cpf)

ronaldo = Pessoa('Ronaldo',32,'123.456.789-00')
ronaldo.beber('cerveja')
ronaldo.beber('refrigerante')
