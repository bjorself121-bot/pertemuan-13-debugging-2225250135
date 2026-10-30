
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi



print("=== TEST CASE ===")

# T1: Rata-rata empat data
hasil = hitung_rata_rata([80, 60, 90, 70])
print("T1 - Rata-rata 4 data:", hasil, "|", "PASS" if hasil == 75.0 else "FAIL")

# T2: Rata-rata dua data
hasil = hitung_rata_rata([100, 80])
print("T2 - Rata-rata 2 data:", hasil, "|", "PASS" if hasil == 90.0 else "FAIL")

# T3: Nilai tepat pada batas kelulusan
hasil = status(60)
print("T3 - Status nilai 60:", hasil, "|", "PASS" if hasil == "Lulus" else "FAIL")

# T4: Nilai di bawah batas kelulusan
hasil = status(59)
print("T4 - Status nilai 59:", hasil, "|", "PASS" if hasil == "Tidak lulus" else "FAIL")

# T5: Mencari nilai tertinggi
hasil = nilai_tertinggi([80, 60, 90, 70])
print("T5 - Nilai tertinggi:", hasil, "|", "PASS" if hasil == 90 else "FAIL")
