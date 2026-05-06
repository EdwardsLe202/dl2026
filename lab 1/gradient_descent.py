def f(x):
    return x**2

def f_prime(x):
    return 2*x

def gradient_descent( x, lr, num_iteration ):
    for i in range(num_iteration):
        x -= lr * f_prime(x)
    return x
    

if __name__ == '__main__':
    x = 10
    lr = 0.1
    num_iteration = 10
    x = gradient_descent(x, lr, num_iteration)   
    print(x) 