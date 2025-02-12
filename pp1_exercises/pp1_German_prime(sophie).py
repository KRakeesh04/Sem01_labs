# p is a prime and 2p+1 is als prime
def is_prime(num) :
    if num == 2 :
        return True
    elif num > 1 :
        for i in range(2,int(num**(1/2)+1)) :
            if num%i == 0 :
                return False
            else :
                continue
        return True
    


range01 = int(input())
range02 = int(input())
total = 0
for j in range(range01,range02+1) :
    if ( is_prime(j) == True ) and ( is_prime(j*2 + 1) == True ) :
        total += j
    else :
        continue

print(total)