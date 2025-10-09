# Name:Roshan Yadav
# Roll no:2311144
# Assignment: Simpson and Monte Carlo Integration

from Func_lib_for_assgn_11 import *

#For Question_1:
print("Doing Question no 1")
# For accuracy upto 6 decimal places by Midpoint point method N=

#For f(x)=1/x
Q_1M_1=midpoint_int(t=1,a=1,b=2,N=1582)
print(f"Integartion result of f(x)=1/x by mid point method accurate upto six decimal places = {Q_1M_1}\n")
# For f(x)=xcos(x)
Q_1M_2=midpoint_int(t=2,a=0,b=(math.pi)/2,N=680)
print(f"Integartion result of f(x)=xcos(x) by Simpson method accurate upto six decimal places = {Q_1M_2}\n")

# For accuracy upto 6 decimal places by Simpson method

#For f(x)=1/x
Q_1S_1=simpson_int(t=1,a=1,b=2,N=33)
print(f"Integartion result of f(x)=1/x by mid point method accurate upto six decimal places = {Q_1S_1}\n")

# For f(x)=xcos(x)
Q_1S_2=simpson_int(t=2,a=0,b=(math.pi)/2,N=16)
print(f"Integartion result of f(x)=xcos(x) by Simpson method accurate upto six decimal places = {Q_1S_2}\n")


# For Question 2:
print("Doing question no 2")
Q_2Mon_3=monte_carlo_int(t=3,a=-1,b=1,k=0.9651217631279374)

print(f"Integartion result of f(x)=(sin(x))^2 by Monte carlo method accurrate upto 3 decimal places = {Q_2Mon_3}")
