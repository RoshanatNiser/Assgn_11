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
    where w(x_n)=h for all n given h=(b-a)/2.'''
    
    # Finding h
    h=(b-a)/N

    # Intialising the result
    r=0

    for i in range(1,N):
        # Finding x_n
        x=(2*a+i*h)/2

        # Summation step
        r=r+h*(f(t,x))
    
    return r

def simpson_int(t,a,b,N):
    '''This does Numerical intergartion of f(x) from a to b
    using Midpoint method. 

    Formula used: 
    S_n= summation w(x_n)*f(x_n) from n=1 to n=N
    where w(x_0)=w(x_N)=h/3, w(x_i)=2h/3 for all even i and w(x_j)=4h/3 for odd j given h=(b-a)/N.'''

    #Find h
    h=(b-a)/N

    #Intialising the result
    r=0

    # Summation loop for summation of w(x_n)*f(x_n) from n=1 to N
    for i in range(0,N+1):

        # Finding x_i
        x=a+i*h

        # Finding weight
        if i==0 or i==N:
            w=h/3
        if i%2==0:
            w=2*h/3
        if i%2!=2:
            w=4*h/3
        
        # Summation step
        r=r+w*f(t,x)

    return r

def pRNG(s=0.1, c=3.95, n=100):
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

def monte_carlo_int(t,a,b,k):
    """This Function does Monte Carlo integartion."""
    r=0
    t=0
    o=0
    R=[]
    O=[]
    N=1
    M=[]

    while (abs(k-r)) > 0.00001:
        N=N*10
        L=pRNG(n=N)
        for i in range(1,N+1):
            x=a+(b-a)*float(L[i])
            print(x)
            print(f(t,x))

            r = r + ((b-a)/N)*(f(t,x))
            t = t + ((1/N)*(f(t,x))**2)

        o=t-((1/(b-a))*r)**2
        R.append(r)
        O.append(o)
        M.append(N)

    # Create Plot of F_n vs N for Monte Carlo Integration
    plt.figure(figsize=(8,6))
    plt.scatter(R,M,alpha=0.5,s=0.5,color='blue')
    plt.xlabel("N")
    plt.ylabel("F_N")
    plt.title("Plot of F_n vs N for Monte Carlo Integration")

    # Save the plot
    plt.savefig(f"Assgn_11_Monte_Carlo.png", dpi=300, bbox_inches='tight')

    return R[len(R)-1]


    

