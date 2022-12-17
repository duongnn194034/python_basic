def tri(a, b, c):
    if(a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b):
        p = (a + b + c)/2
        s = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
        print('S=', s)
    else:
        print(a,',',b,',',c,'không là 3 cạnh của tam giác')

tri(3,4,5)
tri(1,1,4)
tri(4,5,6)



