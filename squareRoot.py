def squareRoot(n):
    # x_(n+1) = 1/2 * (x_n + k / x_n)
    # one can prove that this series converge to squareRoot of k
    # if x_0 > squareRoot(k)

    # Starting point must be greater than squareRoot 
    #of the point, thus we start adding one to n
    #since n could be <1 and in this case 
    #squareRoot of n will be greater than n so we are eliminating 
    #this case by doing this

    x = n + 1 
    err = 0.001
    iteration = 0

    while True:
        iteration += 1
        x_next = 0.5 * (x + n / x)

        if x - x_next < err:
            break
            
        x = x_next
    
    return x, iteration


number = 3
x,i = squareRoot(number)
print('squareRoot of {} is {} \ntakes {} iterations'.format(number, x,i))
