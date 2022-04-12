l1 = [4,8,3,7,2,12,1,9,11,10]

def find_k(list, k):    # k=3 resolve o problema do item 1
    n = len(list)
    j = 0
    while j<k:
        b = list[0]
        b_i = 0
        for i in range(1, n-j):
            if list[i]>b:
                b_i = i
                b = list[i]
        aux = list[b_i]
        list[b_i] = list[n-j-1]
        list[n-j-1] = aux
        j+=1

    return list[-k]

