import sys

def twoN(n):
    if n == 0:
        return 1
    else:
        return twoN(n-1) + twoN(n-1)

def twoNlinear(n):
    product = 1
    for i in range(n):
        product *= 2
    return product

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print (twoNlinear(int(sys.argv[1])))
