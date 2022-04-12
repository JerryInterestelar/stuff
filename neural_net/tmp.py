import nn

rede = nn.Network(2,3,1)

nos = [rede.i_nodes, rede.h_nodes, rede.o_nodes]
biases = [rede.bias_ih, rede.bias_ho]
pesos = [rede.weigth_ih, rede.weigth_ho]

rede = [nos, biases, pesos]

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
