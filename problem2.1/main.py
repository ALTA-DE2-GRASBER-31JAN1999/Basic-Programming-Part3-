def faktor(bilangan):
    faktor = []
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            faktor.append(i)

    for faktor_bilangan in faktor:
        print(faktor_bilangan)

bilangan = int(input("Masukkan bilangan: "))
faktor(bilangan)