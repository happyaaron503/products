#讀取檔案
products = [] #大清單
with open('products.csv', 'r', encoding = 'utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        s = line.strip().split(',') #字串切割，以逗點分
        name = s[0]
        price = s[1]
        #name, price = line.strip().split(',')
        products.append([name, price])
print(products)

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': #quit
        break
    price = input('請輸入商品價格: ')
    p = [] #小清單
    p.append(name)
    p.append(price) #price is str
    price = int(price)
    #p = [name, price]
    products.append(p)
    #products.append([name, price])

for p in products:
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f: #txt改csv, 可用excel開啟
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') #csv用逗點做區隔

