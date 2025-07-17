#This is a 32-bit integer reversal Algorithm. The number ranges from {-2^31 to 2^31-1}. Returns 0 if i/p or o/p not in the range
# Time complexity:O(n) 
# Space Complexity:O(1) 

def reverse(x):
        #Check if Input is 32 bit
        if x <-2**31 or x > (2**31)-1:
            return 0
    
        x_abs = abs(x)
        Rev_num = 0
        while x_abs!=0:
            rem = int(x_abs%10)
            x_abs=(x_abs//10)
            Rev_num =  Rev_num*10+ rem  
        
        if x<0:
            Rev_num = -Rev_num

        #Check if output is 32 bit
        if Rev_num <-2**31 or Rev_num > (2**31)-1:
            return 0

        return Rev_num


print(reverse(-4297))



