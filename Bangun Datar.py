                        # UAS PEMROGRAMAN
# Nama  : ISTIQOMAH
# NPM   : 250305012
# Kelas : 1B Pendidikan Informatika


nama = input("Masukkan Nama Anda: ")

# 1. PERSEGI
def luas_persegi(sisi): 
    return sisi * sisi
def keliling_persegi(sisi):
    return 4 * sisi

# 2. PERSEGI PANJANG
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar
def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

# 3. SEGITIGA
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
def keliling_segitiga(sisi_a, sisi_b, sisi_c):
    return sisi_a + sisi_b + sisi_c

# 4. LINGKARAN
def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari **2
def keliling_lingkaran(jari_jari):
    return 2 * 3.14 * jari_jari

# 5. JAJAR GENJANG
def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi 
def keliling_jajar_genjang(alas, sisi_miring):
    return 2 * (alas + sisi_miring)

# 6. LAYANG-LAYANG
def luas_layang_layang(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2
def keliling_layang_layang(sisi_a, sisi_b):
    return 2 * (sisi_a + sisi_b)

# 7. TRAPESIUM
def luas_trapesium(sisi_a, sisi_b, tinggi):
    return 0.5 * (sisi_a + sisi_b) * tinggi
def keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_d):
    return sisi_a + sisi_b + sisi_c + sisi_d

print("Halo", nama, ", selamat datang di Program Bangun Datar.")

while True:

    menu = [
    "1. Persegi",
    "2. Persegi Panjang",
    "3. Segitiga",
    "4. Lingkaran",
    "5. Jajar Genjang",
    "6. Layang-Layang",
    "7. Trapesium"
    ]

    print("Pilih Bangun Datar yang Ingin Dihitung:")
    print(menu[0])
    print(menu[1])
    print(menu[2])
    print(menu[3])
    print(menu[4])
    print(menu[5])
    print(menu[6])

    pilihan = int(input("Pilih bangun datar (1-7): "))

    if pilihan == 1:
        sisi = int(input("Masukkan panjang sisi persegi: "))
        print("Luas Persegi:", luas_persegi(sisi))
        print("keliling Persegi:", keliling_persegi(sisi))

    elif pilihan == 2:
        panjang = int(input("Masukkan panjang persegi panjang: "))
        lebar = int(input("Masukkan lebar persegi panjang: "))
        print("Luas Persegi Panjang:", luas_persegi_panjang(panjang, lebar))
        print("Keliling Persegi Panjang:", keliling_persegi_panjang(panjang, lebar))

    elif pilihan == 3:
        alas = int(input("Masukkan alas segitiga: "))
        tinggi = int(input("Masukkan tinggi segitiga: "))
        sisi_a = int(input("Masukkan sisi a segitiga: "))
        sisi_b = int(input("Masukkan sisi b segitiga: "))
        sisi_c = int(input("Masukkan sisi c segitiga: "))
        print("Luas Segitiga:", luas_segitiga(alas, tinggi))
        print("Keliling Segitiga:", keliling_segitiga(sisi_a, sisi_b, sisi_c))

    elif pilihan == 4:
        jari_jari = int(input("Masukkan jari-jari lingkaran: "))
        diameter = 2 * jari_jari
        print("Diameter Lingkaran:", diameter)
        print("Luas Lingkaran:", luas_lingkaran(jari_jari))
        print("Keliling Lingkaran:", keliling_lingkaran(jari_jari))

    elif pilihan == 5:
        alas = int(input("Masukkan alas jajar genjang: "))
        tinggi = int(input("Masukkan tinggi jajar genjang: "))
        sisi_miring = int(input("Masukkan sisi miring jajar genjang: "))
        print("Luas Jajar Genjang:", luas_jajar_genjang(alas, tinggi))
        print("Keliling Jajar Genjang:", keliling_jajar_genjang(alas, sisi_miring))

    elif pilihan == 6:
        diagonal1 = int(input("Masukkan diagonal 1 layang-layang: "))
        diagonal2 = int(input("Masukkan diagonal 2 layang-layang: "))
        sisi_a = int(input("Masukkan sisi a layang-layang: "))
        sisi_b = int(input("Masukkan sisi b layang-layang: "))
        print("Luas Layang-Layang:", luas_layang_layang(diagonal1, diagonal2))
        print("Keliling Layang-Layang:", keliling_layang_layang(sisi_a, sisi_b))

    elif pilihan == 7:
        sisi_a = int(input("Masukkan sisi a trapesium: "))
        sisi_b = int(input("Masukkan sisi b trapesium: "))
        sisi_c = int(input("Masukkan sisi c trapesium: "))
        sisi_d = int(input("Masukkan sisi d trapesium: "))
        tinggi = int(input("Masukkan tinggi trapesium: "))
        print("Luas Trapesium:", luas_trapesium(sisi_a, sisi_b, tinggi))
        print("Keliling Trapesium:", keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_d))

    else:
        print("Pilihan tidak tersedia")

    lagi = input("Apakah Anda ingin menghitung bangun datar lain? (ya/tidak): ")
        
    if lagi == "ya":
        continue

    else:
        print("Terima Kasih Telah Menggunakan Program Ini")
        break