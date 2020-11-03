from sys import exit
while True:
    while True:
        try:
            a = int(input("\nangka pertama: "))
            b = int(input("angka kedua: "))
            break
        except ValueError:
            print("masukkan angka")
            continue
    print("1. tambah\n2. kurang\n3. kali\n4. bagi\n5. modulus(sisa bagi)\n6. Pangkat")

    while True:
        try:
            opsi = int(input("masukkan pilihan: "))
            if opsi < 0 or opsi >6:
                print("masukkan pilihan yang sesuai")
                continue
            elif opsi == 0:
                print("masukkan pilihan yang sesuai")
                continue
            else:
                break
        except ValueError:
            print("masukkan pilihan yang sesuai")
            continue
    
    if opsi == 1:
        c = a+b
        cc = "+"
    elif opsi == 2:
        c = a-b
        cc = "-"
    elif opsi == 3:
        c = a*b
        cc = "x"
    elif opsi == 4:
        c = a/b
        cc = "/"
    elif opsi == 5:
        c = a%b
        cc = "%"
    elif opsi == 6:
        c = 1
        for i in range(b):
            c *= a
        cc = "^"

    if opsi == 6:
        for i in range(b-1):
            print(f"{a} x ", end='')
        print(f"{a} = {c}", f"\n({a} {cc} {b} = {c})")
    else:
        print(f"\nhasil dari {a} {cc} {b} = {c}")

    while True:
        opsi = input("\nulangi? (Y/N) ")
        if opsi == 'Y' or opsi == 'y':
            break
        elif opsi == 'N' or opsi == 'n':
            print('keluar')
            exit()
        else:
            print('pilih (Y/N)')
            continue