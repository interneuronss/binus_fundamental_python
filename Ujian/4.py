"""
Buat sebuah fungsi rerata_nilai_mhs yang menampilkan nilai-nilai praktikum dari seorang mahasiswa yang
diberikan sebagai parameter. Sebagai contoh, pemanggilan fungsi rerata_nilai_mhs('Icha', dataDict)
akan menghasilkan output  sebagai berikut
80 70 70 80
Rerata = 75

"""


def rerata_nilai_mhs(nama, dataDict):
    if nama in dataDict:
        nilai_list = dataDict[nama]

        print(nilai_list)

        rerata = sum(nilai_list) / len(nilai_list)
        print(f"Rerata = {rerata}")
    else:
        print(f"Data {nama} tidak ditemukan.")

dataDict = {
    'Icha': [80, 70, 70, 80]
}

nama = input("Masukan nama: ")

if nama not in dataDict:
    daftar = input("Mahasiswa belum terdaftar. Apakah ingin didaftarkan? (Ya/Tidak): ")
    if daftar.lower() == "ya":
        list_nilai = []
        status = True
        while status:
            input_nilai = input(f"Masukan nilai {nama} (tekan Enter jika selesai): ")
            if input_nilai == "":
                status = False
            else:
                list_nilai.append(int(input_nilai))

        if list_nilai:
            dataDict[nama] = list_nilai
            rerata_nilai_mhs(nama, dataDict)
else:
    rerata_nilai_mhs(nama, dataDict)






