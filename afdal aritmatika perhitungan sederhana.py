def tambahkan(x, y):
    return x + y

def kurangi(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa membagi dengan nol!"

def main():
    print("Pilih operasi yang ingin dilakukan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print(f"Hasil {num1} + {num2} = {tambahkan(num1, num2)}")
    elif pilihan == '2':
        print(f"Hasil {num1} - {num2} = {kurangi(num1, num2)}")
    elif pilihan == '3':
        print(f"Hasil {num1} * {num2} = {kali(num1, num2)}")
    elif pilihan == '4':
        print(f"Hasil {num1} / {num2} = {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()