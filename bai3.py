T = float(input('Nhập số tiền gửi (triệu đồng): '))
S = T
for i in range(1, 11):
    S = S * 1.1
    print('Số tiền cả vốn lẫn lãi sau năm thứ', i,'là',S,'triệu đồng')