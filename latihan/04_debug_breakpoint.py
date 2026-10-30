
def hitung_total(daftar_nilai):
    total = 0

    for nilai in daftar_nilai:
        total += nilai

    return total


nilai_mahasiswa = [80, 60, 90, 70]
total_nilai = hitung_total(nilai_mahasiswa)
rata_rata = total_nilai / len(nilai_mahasiswa)

print("Daftar nilai:", nilai_mahasiswa)
print("Total nilai:", total_nilai)
print("Rata-rata:", rata_rata)
