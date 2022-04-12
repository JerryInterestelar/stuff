#Dados a serem salvados
nome = 'Rodrigo'
idade = 35

#faz ou abre um arquivo chamado 'Minibank.py'
f = open("Minibank.py", "w")

#gravar um string necessita que '' sejam escritas
f.write("nome = '" + str(nome) + "'\n")
f.write("idade = " + str(idade) + "\n")
f.close()
