for i in range(100):

    if i==99:
         print('{} '.format(i))
    elif i<10:
        print('0{}'.format(i))

    else:
         print('{}, '.format(i) ,end='\n')