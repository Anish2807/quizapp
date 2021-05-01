import random as r
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
        
    print("your one time otp is ",otp)
otpgen()
print(b)

