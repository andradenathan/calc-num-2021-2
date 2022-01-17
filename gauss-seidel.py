def gauss_seidel(x, a, b):   
    linhas = len(a)                   
    for i in range(0, linhas):        
        d = b[i]                  
        for j in range(0, linhas):     
            if(i != j):
                d-=a[i][j] * x[j]       
        x[i] = d / a[i][i]  
    return x