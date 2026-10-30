# Praktikum 4 — Debugging, Tracing, dan Testing Python

## Identitas Mahasiswa

- **Nama:** Muhammad Fatih Ammar
- **NIM:** 2225250135
- **Kelas:** 3E
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Pertemuan:** 13

## 1. Deskripsi Praktikum

Praktikum ini bertujuan untuk memahami proses debugging, tracing, dan testing pada program Python. Pengujian dilakukan untuk menemukan kesalahan, menganalisis penyebabnya, memperbaiki kode, dan memastikan hasil program sesuai dengan yang diharapkan.

## 2. Kasus yang Diuji

Program utama berada pada file `praktik/praktik_4_debugging.py`. Program memiliki tiga fungsi utama, yaitu menghitung rata-rata, menentukan status kelulusan, dan mencari nilai tertinggi.

Data awal yang digunakan adalah `[80, 60, 90, 70]`.

## 3. Bug Report

### Bug 1 — Perhitungan Rata-rata

- **Jenis bug:** Logical error
- **Penyebab:** Program membagi jumlah nilai dengan angka tetap 5.
- **Dampak:** Hasil rata-rata tidak sesuai dengan jumlah data sebenarnya.
- **Perbaikan:** Mengganti pembagi tetap dengan `len(nilai)`.

### Bug 2 — Status Kelulusan

- **Jenis bug:** Logical error
- **Penyebab:** Kondisi menggunakan `nilai > 60`.
- **Dampak:** Nilai tepat 60 dinyatakan tidak lulus.
- **Perbaikan:** Menggunakan kondisi `nilai >= 60`.

### Bug 3 — Nilai Tertinggi

- **Jenis bug:** Logical error
- **Penyebab:** Variabel awal menggunakan nilai 0 dan kondisi perbandingan menggunakan operator `<`.
- **Dampak:** Program menghasilkan nilai tertinggi yang salah.
- **Perbaikan:** Menginisialisasi nilai tertinggi dengan elemen pertama dan membandingkan menggunakan operator `>`.

## 4. Test Case dan Hasil Retest

| ID | Pengujian | Input | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|---|---|
| T1 | Rata-rata 4 data | `[80, 60, 90, 70]` | `75.0` | `75.0` |
| T2 | Rata-rata 2 data | `[100, 80]` | `90.0` | `90.0` |
| T3 | Batas kelulusan | `60` | `Lulus` | `Lulus` |
| T4 | Di bawah batas kelulusan | `59` | `Tidak lulus` | `Tidak lulus` |
| T5 | Nilai tertinggi | `[80, 60, 90, 70]` | `90` | `90` |

**Status pengujian:** Isi status PASS setelah memastikan kelima test case berhasil dijalankan dan hasil aktual sesuai dengan hasil yang diharapkan.

## 5. Cara Menjalankan Program

Jalankan perintah berikut dari direktori utama proyek:

```bash
python praktik/praktik_4_debugging.py
```

Program akan menampilkan hasil lima test case beserta status pengujiannya.

## 6. Refleksi

Melalui praktikum ini, saya mempelajari bahwa program yang dapat berjalan belum tentu menghasilkan keluaran yang benar. Kesalahan logika perlu ditemukan melalui pengujian dengan berbagai input. Saya juga belajar membandingkan hasil aktual dengan hasil yang diharapkan, menemukan akar penyebab bug, melakukan perbaikan, dan menjalankan kembali pengujian untuk memastikan perbaikan berhasil.

## 7. Kesimpulan

Tiga bug logika pada program utama telah dianalisis dan diperbaiki. Keberhasilan perbaikan dibuktikan melalui lima test case yang mencakup perhitungan rata-rata, batas kelulusan, dan pencarian nilai tertinggi.