# Name:Roshan Yadav
# Roll no:2311144
# Assignment: Simpson and Monte Carlo Integration

import math
import matplotlib.pyplot as plt

def f(t,x):
    if t==1:
        return 1/x
    if t==2:
        return x*(math.cos(x))
    if t==3:
        return (math.sin(x))**2

def midpoint_int(t,a,b,N):
    '''This does Numerical intergartion of f(x) from a to b
    using Midpoint method. 

    Formula used: 
    M_n= summation w(x_n)*f(x_n) from n=1 to n=N
    where w(x_n)=h for all n given h=(b-a)/N.'''
    
    # Finding h
    h=(b-a)/N

    # Intialising the result
    r=0

    for i in range(1,N+1):
        # Finding x_n
        x=a+(i-0.5)*h

        # Summation step
        r=r+h*(f(t,x))
    
    return r

def simpson_int(t,a,b,N):
    
    '''This does Numerical intergartion of f(x) from a to b
    using Simpson method. 

    Formula used: 
    S_n= summation w(x_n)*f(x_n) from n=0 to n=N
    where w(x_0)=w(x_N)=h/3, w(x_i)=2h/3 for all even i and w(x_j)=4h/3 for odd j given h=(b-a)/N.'''

    #Find h
    h=(b-a)/N

    #Intialising the result
    r=0

    # Summation loop for summation of w(x_n)*f(x_n) from n=0 to N
    for i in range(0,N+1):

        # Finding x_i
        x=a+i*h

        # Finding weight
        if i==0 or i==N:
            w=h/3
        elif i%2==0:
            w=2*h/3
        else:
            w=4*h/3
        
        # Summation step
        r=r+w*f(t,x)

    return r

def pRNG(s=0.123456789, c=3.9, n=10000):
    '''This function is a Pseudo random number generator 
    which uses equation x(i+1) = c*x(i)*(1-x(i)), 
    where x(0)=s and c are given as input.
    Returns a list of n random numbers'''

    L = []
    L.append(s)  # x(0) = s
    
    for i in range(n-1):
        t = c * L[i] * (1 - L[i])  # x(i+1) = c*x(i)*(1-x(i))
        L.append(t)
    
    return L

def monte_carlo_int(t, a, b, v, max_iter=30):

    """This Function does Monte Carlo integartion. 
    It gives the answer accurate upto 3 decimal places 
    as discussed in the class."""

    R = []
    M = []
    N = 100
    iter = 0
    seed = 12345
    
    sum_f = 0
    sum_f2 = 0
    total_samples = 0

    while iter < max_iter:
        iter = iter + 1
        
        seed = (seed * 1103515245 + 12345) % (2**31)
        
        L = pRNG(s=seed, n=N)
        
        for i in range(N):
            x = a + (b-a) * L[i]
            fx = f(t, x)
            
            sum_f = sum_f + fx
            sum_f2 = sum_f2 + fx**2
        
        total_samples = total_samples + N
        
        r = (b-a) * sum_f / total_samples
        k = sum_f2 / total_samples
        o = k - (sum_f / total_samples)**2
        
        R.append(r)
        M.append(total_samples)
        
        if len(R) >= 3 and abs(r - v) < 0.0001:
                break
        
        N = N + 500

    plt.figure(figsize=(8,6))
    plt.plot(M, R, marker='o', markersize=8, color='blue', label='F_N')
    plt.axhline(y=v, color='r', linestyle='--', linewidth=2, label=f'Target={v:.4f}')
    plt.xlabel("N")
    plt.ylabel("F_N")
    plt.title("Plot of F_n vs N for Monte Carlo Integration")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f"Assgn_11_Monte_Carlo.png", dpi=300, bbox_inches='tight')
    plt.close()

    return R[-1]

