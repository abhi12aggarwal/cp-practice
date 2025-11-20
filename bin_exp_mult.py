import sys

def bin_mult(a:int,b:int,mod:int)->int:
    #sys.stdout.write(f"a: {a}, b:{b}, ")
    
    a%=mod
    b%=mod
    
    
    
    result = 0
    while b>0:
        if b&1:
            result = (result + a)%mod
        a = (a<<1)%mod
        b = b>>1
    
    #sys.stdout.write(f"result: {result}\n")
    return result
    
    
def bin_exp(a:int, b:int, mod:int)->int:
    a%=mod
    result = 1
    while b>0:
        if b&1:
            sys.stdout.write(f"b: {b};\t")
            sys.stdout.write(f"{result} * {a} % {mod} = ")
            result = bin_mult(result,a,mod)
            sys.stdout.write(f"{result}\n")
        a = bin_mult(a,a,mod)
        b = b>>1
        
    return result
    
    
def main():
    ##  sys.stdout.write(f"{bin_mult(int(1e5),int(1e5),int(1e9)+7)}")
    sys.stdout.write(f"{bin_exp(int(1e5),int(1e3),int(1e9)+7)}")
    
if __name__=='__main__':
    main()