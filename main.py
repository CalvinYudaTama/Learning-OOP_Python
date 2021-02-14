"""
Belajar OOP
"""
from geometri.bangunruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menghitung Luas Persegi Panjang')

p1 = PersegiPanjang(10, 3)

print(p1.info())
print(p1.hitung_luas())

print('\nMengitung Luas Segitiga')

p2 = Segitiga(10, 4)

print(p2.info())
print(p2.hitung_luas())

print('\nMencoba Memanggil Object Dari Class BangunRuang')

b1 = BangunRuang()

print(b1.info())
print(b1.hitung_luas())


print('\nPolymorphism')
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(p2)

for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
