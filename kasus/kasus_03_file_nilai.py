
def baca_nilai(nama_file):
    nilai = []

    with open(nama_file, "r") as file:
        for baris in file:
            nilai.append(int(baris.strip()))

    return nilai


print(baca_nilai("data/nilai.txt"))
