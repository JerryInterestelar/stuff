import random 
import nn
#pre valores ajudantes "teste XOR"
nn = nn.Network(2,3,1)
input = [[1,1],[1,0],[0,1],[0,0]]
output = [[0],[1],[1],[0]]

def print_bias(net):
    biases = [net.bias_ih, net.bias_ho]

    l = 2
    for layer in biases:
        print('camada ', l)
        n = 1
        for bias in layer:
            print(f'bias {bias[0]} neuronio {n}')
            n+=1
            print()
        l+=1
        print()

def print_weigth(net):
    pesos = [net.weigth_ih, net.weigth_ho]
    
    l = 2
    for layer in pesos:
        print('camada ', l)
        n = 1
        for neuron in layer:
            print('neuronio ', n)
            c = 1
            for conn in neuron:
                #conexao do neuronio L com neuronio L-1
                print (f'conexao do neuronio {c} com neuronio {n}')
                print(conn)
                c+=1
            n+=1
            print()
        l+=1
        print()

def test(nn, input, output):
    while True:
        i = 0
        while i<10000: 
            index = random.randint(0,3)
            nn.train(input[index], output[index])
            i+=1
        print(nn.predict([0,0])[0][0], nn.predict([1,0])[0][0])
        if nn.predict([0,0])[0][0] < 0.04 and nn.predict([1,0])[0][0] > 0.98:
            print('terminou')
            return nn
