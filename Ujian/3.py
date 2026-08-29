"""
SOAL 3
Buat sebuah fungsi dengan nama “terbesar” yang menerima parameter tiga bilangan bulat dalam urutan sembarang
(tidak harus terurut). Fungsi ini akan mengembalikan bilangan terbesar dari ketiga bilangan yang diberikan.
Contoh pemanggilan fungsi:
print(terbesar(3, 8, 4)) # menghasilkan output 8

"""

def terbesar(num1, num2, num3):
    return max(num1, num2, num3)

print(terbesar(3, 8, 4))
