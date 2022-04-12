l = [3,5,4,6,1,2,7,9,8]
def busca(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
           return i 
    return False


def encontra_p(lista, valor):   
    #ao que parece funciona entao deixa quieto
    n = len(lista) 
    res = busca(lista, valor)
    v_enc = lista[res]
    if res != False:
        m_prox = 0
        m_ind = 0
        for i in range(n):
            c_atual = lista[i]
            if c_atual != v_enc:
                mp_atual = abs(v_enc-m_prox)
                comp_atual = abs(v_enc-c_atual)
                if comp_atual < mp_atual:
                    m_prox = c_atual      
                    m_ind = i
        return m_prox, m_ind
    else:
        return "Este valor nao esta na lista"

