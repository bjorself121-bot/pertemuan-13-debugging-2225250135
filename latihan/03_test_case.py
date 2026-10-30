
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_cases = [
    (75, "Lulus"),
    (60, "Lulus"),
    (59, "Tidak lulus"),
    (0, "Tidak lulus"),
    (100, "Lulus"),
]

for nomor, (nilai, harapan) in enumerate(test_cases, start=1):
    aktual = status_lulus(nilai)
    status_tes = "PASS" if aktual == harapan else "FAIL"

    print(
        f"T{nomor}: nilai={nilai}, "
        f"harapan={harapan}, aktual={aktual} -> {status_tes}"
    )
