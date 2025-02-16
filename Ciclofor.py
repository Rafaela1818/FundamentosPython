# Ciclo FOR- tabuada

for i in range (1, 11): # outer loop
    #nested loop
    #iterações de 1 to 10
    for j in range(1,11):
        #print multiplication 
        multiplicacao = i * j
        print("%d*%d=%d\n"%(i, j, multiplicacao))
    print("concluido")