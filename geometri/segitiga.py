from geometri.bangunruang import BangunRuang


class Segitiga(BangunRuang):

    def __init__(self, a, t):
        self.a = a
        self.t = t

    def info(self):
        return (f'Menghitung Luas Segitiga Dengan Alas = {self.a} Dan Tinggi = {self.t}')

    def hitung_luas(self):
        return self.a * self.t / 2