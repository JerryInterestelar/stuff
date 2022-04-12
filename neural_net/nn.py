import numpy as np
import math

#Primeiro modelo de rede neural de 3 camadas, algoritimo feito por Jose Bezerra, adpatado por mim (não que seja muita coisa)

def dSigmoid(x):
	return x*(1-x)

def sigmoid(x):
	return 1 /(1 + math.exp(-x))

class Network:
	def __init__(self, i_nodes, h_nodes, o_nodes):
		self.i_nodes = i_nodes		#Nos de entrada, camada escondida e saida respectivamente
		self.h_nodes = h_nodes
		self.o_nodes = o_nodes
	
		self.bias_ih = np.random.rand(self.h_nodes, 1)
		self.bias_ho = np.random.rand(self.o_nodes, 1)
	
		self.weigth_ih = np.random.rand(self.h_nodes, self.i_nodes)
		self.weigth_ho = np.random.rand(self.o_nodes, self.h_nodes)	#pesos tambem "semi" aleatorios
	
		self.learning_rate = 0.1
	
	def feedForward(self, i):		#input é uma matriz
		
		vsig = np.vectorize(sigmoid)		#transformando a funcao em uma funcao "mapeadora" (sla mano)

		#INPUT - HIDDEN 
		input = np.array(i).reshape((len(i), 1))
		hidden = self.weigth_ih @ input  	#dot product
		hidden = hidden + self.bias_ih		#incrementando a camada com o bias
		nHidden = vsig(hidden)			#normalizando

		#HIDDEN - OUTPUT
		output = self.weigth_ho @ nHidden	#msm coisa da INPUT HIDDEN
		output = output + self.bias_ho
		nOutput = vsig(output)
		
		return input, nHidden, nOutput

	def train(self, i, target):

		vdsig = np.vectorize(dSigmoid)
			
		#OUTPUT - HIDDEN
		expected = np.array(target).reshape((len(target), 1))
		input, hidden, output = self.feedForward(i)

		output_error = expected - output		#(1)||
		d_output = vdsig(output)
		t_hidden = np.transpose(hidden)
		
		gradient = d_output * output_error
		ngradient = gradient * self.learning_rate	#ngrandient = gradiente "normalizado"
		
		self.bias_ho = self.bias_ho + gradient		#Ajuste do bias h-o

		d_weigth_ho = ngradient @ t_hidden		#correçoes para os pesos da camada oculta para a saida
		self.weigth_ho = self.weigth_ho + d_weigth_ho	#aplicaçao das correcoes
		
		#HIDDEN - INPUT
		weigth_ho_t = np.transpose(self.weigth_ho)

		hidden_error = weigth_ho_t @ output_error	#!!!!Nao entedi direito pq e assim
		d_hidden = vdsig(hidden)			#Daqui pra frente e igual ao processo anterior(1)
		
		gradient_h = hidden_error * d_hidden
		ngradient_h = gradient_h * self.learning_rate
		t_input = np.transpose(input)	

		self.bias_ih = self.bias_ih + gradient_h

		d_weigth_ih = ngradient_h @ t_input
		self.weigth_ih = self.weigth_ih + d_weigth_ih

		#return self.weigth_ih, d_weigth_ih, self.weigth_ho, d_weigth_ho
	def predict(self, i):

		return self.feedForward(i)[2]

