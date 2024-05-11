class MinhaClasse:

    estático = 'lhama'

    def __init__ (self,estado):
        self.estado = estado
    def print_estatico(self):
        estático = 9
        print(self.estático)

obj1 = MinhaClasse(True)
obj1.print_estatico()
