for i in range(10):
    for j in range(10):
        if j!=i:
            if i < j:
                print('{}{}, '.format(i,j), end='\n')