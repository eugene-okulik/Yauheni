PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


price_list_dict = {
    product: int(price.removesuffix('р'))
    for product, price in (line.split() for line in PRICE_LIST.split('\n'))
}

print(price_list_dict)
