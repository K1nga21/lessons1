buyurtmalar = ['olma','anor','uzum','banan']
mahsulotlar = {'olma':26580,
               'shaftoli':25000,
               'qovun':18000,
               'banan':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
