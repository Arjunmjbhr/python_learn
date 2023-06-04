# return the gcd of 2 numbers

def gcd(n1, n2):
    gcd = 1 # Initial GCD is 1
    k = 2  # possible GCD

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # update GCD
        k += 1
        
    return gcd # return gcd
