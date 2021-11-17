import unittest

def roman(x):
    if type(x) != int:
        raise Exception("wrong type")
    wynik = ""
    while x != 0:
        if x / 1000 >= 1:
            wynik += ("M" * (x // 1000))
            x -= (x // 1000) * 1000
        if x / 500 >= 1 and x // 900 != 1:
            wynik += ("D" * (x // 500))
            x -= (x // 500) * 500
        if x // 900 == 1:
            wynik += ("CM")
            x -= 900
        if x // 100 >= 1 and x // 100 <= 3:
            wynik += ("C" * (x // 100))
            x -= (x // 100) * 100
        if x // 100 == 4:
            wynik += ("CD")
            x -= 400
        if x / 50 >= 1 and x // 90 != 1:
            wynik += ("L" * (x // 50))
            x -= (x // 50) * 50
        if x // 90 == 1:
            wynik += ("XC")
            x -= 90
        if x / 10 >= 1 and x // 10 <= 3:
            wynik += ("X" * (x // 10))
            x -= (x // 10) * 10
        if x // 10 == 4:
            wynik += ("XL")
            x -= 40
        if x / 5 >= 1 and x // 9 != 1:
            wynik += ("V" * (x // 5))
            x -= (x // 5) * 5
        if x // 9 == 1:
            wynik += ("IX")
            x -= 9
        if x / 1 >= 1 and x // 1 <= 3:
            wynik += ("I" * (x // 1))
            x -= (x // 1) * 1
        if x // 4 == 1:
            wynik += ("IV")
            x -= 4
    return wynik


class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_a_single_i(self):
        self.assertEqual(roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(roman(3), "III")

    def test_4_being_5_1_is_iv(self):
        self.assertEqual(roman(4), "IV")

    def test_5_is_a_single_v(self):
        self.assertEqual(roman(5), "V")

    def test_6_being_5_1_is_vi(self):
        self.assertEqual(roman(6), "VI")

    def test_9_being_10_1_is_ix(self):
        self.assertEqual(roman(9), "IX")

    def test_20_is_two_x_s(self):
        self.assertEqual(roman(27), "XXVII")

    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(roman(48), "XLVIII")

    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(roman(49), "XLIX")

    def test_50_is_a_single_l(self):
        self.assertEqual(roman(59), "LIX")

    def test_90_being_100_10_is_xc(self):
        self.assertEqual(roman(93), "XCIII")

    def test_100_is_a_single_c(self):
        self.assertEqual(roman(141), "CXLI")

    def test_60_being_50_10_is_lx(self):
        self.assertEqual(roman(163), "CLXIII")

    def test_400_being_500_100_is_cd(self):
        self.assertEqual(roman(402), "CDII")

    def test_500_is_a_single_d(self):
        self.assertEqual(roman(575), "DLXXV")

    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(roman(911), "CMXI")

    def test_1000_is_a_single_m(self):
        self.assertEqual(roman(1024), "MXXIV")

    def test_3000_is_three_m_s(self):
        self.assertEqual(roman(3000), "MMM")
