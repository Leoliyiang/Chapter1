response1=input("What's your principal amount?")
P=float(response1)
response2=input("What's your annual nominal interest rate?")
R=float(response2)
response3=input("What's your number of times the interest is compounded per year?")
N=float(response3)
response4=input("What's your number of year?")
T=float(response4)
print("The final amount after t years is ", P*(1+R/N)**(N*T))