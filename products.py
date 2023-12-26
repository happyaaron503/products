products = [] #大清單
while True:
    name = input('請輸入商品名稱')
    if name == 'q': #quit
        break
    price = input('請輸入商品價格')
    p = [] #小清單
    p.append(name)
    p.append(price)
    # p = [name, price]
    products.append(p)
    # products.append([name, price])

for p in products:
    print(p[0], '的價格是', p[1])