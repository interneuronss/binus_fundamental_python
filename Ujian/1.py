"""
SOAL 1

Nyatakan rumus matematika berikut ini dalam sebuah statement bahasa pemrograman Python
(b-10)/(2(1-(a/2y^2)))
Variabel b, a dan y merupakan variabel yang dapat diinput.
"""

b = float(input("b: "))
a = float(input("a: "))
y = float(input("y: "))

rumus = (b - 10) / (2 * (1 - (a / 2 * (y ** 2))))

print("Hasil:", rumus)
