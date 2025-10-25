''' What is diff b|w / vs //

/- division operator
       - Return the result in the form of float type
                  int / int -> float
                  int / float -> float
                  float / int -> float
                  float / float -> float
                  
// - floor division
      - Returns the Result based on the operand types
             int // int -> int
             float // int -> float
             int // float -> float
             float // float -> float
       - It will always return precision  value but not scale
                              3[precision] .14 [scale]             

'''
print("10/3 ? : ",10/3)
print("10/3.0 ? : ",10/3.0)
print("10.0/3 ? : ",10.0/3)
print("10.0/3.0 ? : ",10.0/3.0)
print("====================")

print("10//3 ? : ",10//3)    #10//3 -> 3
print("10//3.0 ? : ",10//3.0)   #10//3.0 -> 3.0
print("10.0//3 ? : ",10.0//3)    #3.0
print("10.0//3.0 ? : ",10.0//3.0) #3.0














