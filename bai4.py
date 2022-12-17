n = int(input('Số lượng virus hiện tại là '))
i = 0
while n <= 1000000:
    n = n * 2
    i = i + 1
print('Sau', i, 'ngày thì số virus vượt quá một triệu.')
