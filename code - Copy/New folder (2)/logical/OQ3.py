#Finding missing number
def missing(lst):
      n=len(lst)+1   #5
      exp_sum= n * (n+1) //2   #15
      act_sum= sum(lst)  #12
      mn=exp_sum-act_sum
      return mn 

#calling
lst=[1,2,4,5]
m=missing(lst)
print("Missing number : ",m)
