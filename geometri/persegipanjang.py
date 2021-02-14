from geometri.bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):

    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return (f'Menghitung Luas Persegi Panjang Dengan Panjang = {self.p} Dan Lebar = {self.l}')

    def hitung_luas(self):
        return self.p * self.l