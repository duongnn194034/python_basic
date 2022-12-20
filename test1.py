a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a <= 0 or b <= 0 or c <= 0:
    print('Mời bạn nhập lại a,b,c>0')
else:
    if a + b <= c or b + c <= a or c + a <= b:
        print('A,b,c không phải là độ dài 3 cạnh tam giác')
    else:
        can = a == b or b == c or c == a
        vuong = a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
        print('Diện tích tam giác là:', s)
        if vuong and can:
            print('Tam giác trên là tam giác vuông cân')
        elif vuong:
            print('Tam giác trên là tam giác vuông')
        elif can:
            print('Tam giác trên là tam giác cân')
