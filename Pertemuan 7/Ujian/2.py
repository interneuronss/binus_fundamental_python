"""
SOAL 2
a.	Jelaskan apa yang dimaksud dengan variabel.
    Variabel adalah nama yang diberikan suatu objek atau value yang ingin di store di dalam memori,
    diberikan dengan simbol =
b. Tuliskan variabel-variabel yang terdapat pada program di atas.
    _t, y2h, x
c. Jelaskan adakah kesalahan pada program di atas, jika ada perbaiki kesalahan yang ada
    - di baris pertama, variabel y2h tidak diberikan value awal.
    - syntax error di baris 3 (kurang : di akhir loop) dan di baris 6 (; diganti jadi :)
    - baris 4 simbol = harusnya == (sama dengan)

"""

y2h = 0
_t = 18
for x in range (5):
    if x % 2 == 0:
        y2h = _t - x
    elif _t > x:
        _t = _t // x
    else:
        y2h = y2h + 1
    print(x, y2h)
