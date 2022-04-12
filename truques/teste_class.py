class Classe:
	def __init__(self):		#construtor
		self.nome = "nome"
		self.lista = [1,3,2,4]
		

	def funcao(self):
		return "hello world"


c = Classe()
print(c.nome)
print(c.lista)
print(c.funcao())	
