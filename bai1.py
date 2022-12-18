N = int(input())
uoc = 0
for i in range(1, N+1):
    if N % i == 0:
        uoc = uoc + 1
print('N có', uoc, 'ước')
print('Các ước là:')
for i in range(1, N+1):
    if N % i == 0:
        print(i)
