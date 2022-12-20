def SNT(x):
    uoc = 0
    for j in range(1,x+1):
        if x % j == 0:
            uoc = uoc + 1
    return uoc == 2

N = int(input('N='))
if N <= 0:
    print('Mời bạn nhập lại N>0')
else:
    tong = 0
    n = 0
    #Đây là tổng số chẵn
    #Số lẻ thì range(1,...)
    for i in range(2, N+1, 2):
        tong = tong + i
        n = n + 1
    print('TBC các số chẵn từ 1 đến N là', tong/n)
    print('Các số nguyên tố từ 1 đến N là')
    for i in range(1, N+1):
        if SNT(i):
            print(i)
