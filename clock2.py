res1=input("What time is it now?") #write three digits like 1:30 is 130
res2=input("What's the number of time to wait?") #as above
N=int(res1)
T=int(res2)
Hours_now=N//100
Minutes_now=N%100
Hours_then=T//100
Minutes_then=T%100
print("The clock will goes of at ", Hours_now+Hours_then, Minutes_now+Minutes_then)