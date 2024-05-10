class Livro():
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def apresentar(self):
        print(f"O livro {self.titulo} foi escrito por {self.autor} em {self.ano}")




livros = []
quer_continuar = 's'
while quer_continuar == 's':
    pergunta_livro = input('Qual o nome do livro?: ')
    pergunta_autor = input('Qual o nome do autor?: ')
    pergunta_ano = input('Qual o ano de publicação?: ')
    livro = Livro(pergunta_livro,pergunta_autor,pergunta_ano)
    livros.append(livro)
    quer_continuar = input('Deseja continuar? (s/n): ')

for livro in livros:
    livro.apresentar()

