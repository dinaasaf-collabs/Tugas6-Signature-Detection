# Tugas 6 - Signature Detection

## Deskripsi
Mini project ini digunakan untuk mendeteksi keberadaan tanda tangan pada citra ijazah.

Sistem membedakan citra menjadi dua kategori:
- SIGNATURE PRESENT
- SIGNATURE ABSENT

Dataset yang digunakan terdiri dari 18 citra, yaitu 9 citra dengan tanda tangan dan 9 citra tanpa tanda tangan.

## Tahapan Pengolahan Citra

Tahapan yang dilakukan dalam sistem adalah:

1. Crop area tanda tangan
2. Konversi citra menjadi grayscale
3. Global Threshold
4. Otsu Threshold
5. Morphological Opening
6. Morphological Closing
7. Menghitung jumlah piksel foreground
8. Menentukan keberadaan tanda tangan berdasarkan nilai threshold
9. Menguji data PRESENT dan ABSENT

## Struktur Folder

```text
Tugas6_Signature_Detection/
│
├── dataset/
│   ├── present/
│   └── absent/
│
├── morphology/
│   ├── opening/
│   └── closing/
│
├── output/
│   ├── crop/
│   ├── grayscale/
│   ├── global_threshold/
│   ├── otsu_threshold/
│   └── morphology/
│
├── main.py
├── tabel_hasil.py
├── hasil_tabel_18_data.txt
└── README.md
## Cara Menjalankan Program

1. Buka folder project `Tugas6_Signature_Detection` di Visual Studio Code.

2. Buka Terminal atau PowerShell pada folder project.

3. Jalankan program utama:

```bash
python main.py

4. Setelah program utama selesai, jalankan program tabel hasil.

Perintah yang digunakan:

python tabel_hasil.py

