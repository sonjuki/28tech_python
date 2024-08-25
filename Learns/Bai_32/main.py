#UCLN => Thuật toán Eculid
#BCNN => a * b/ UCLN

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd(a, b))
    print(lcm(a, b))
