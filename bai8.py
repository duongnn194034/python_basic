def tri(a, b, c):
    if(a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b):
        p = (a + b + c)/2
        return (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    else:
        return 0

print('S=', tri(3,4,5))
print('S=', tri(1,1,4))
print('S=', tri(4,5,6))
print('ST=', tri(3,4,5) + tri(1,1,4) + tri(4,5,6))