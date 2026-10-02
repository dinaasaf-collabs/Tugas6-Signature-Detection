import cv2
import os
import glob
import numpy as np

# ==========================================================
# FOLDER
# ==========================================================
PRESENT_FOLDER = "output/morphology/closing"
ABSENT_FOLDER = "dataset/absent"

# ==========================================================
# THRESHOLD HASIL PERHITUNGAN
# ==========================================================
BATAS = 206282.78


# ==========================================================
# FUNGSI ANALISIS
# ==========================================================
def hitung_foreground(path):

    image = cv2.imread(
        path,
        cv2.IMREAD_GRAYSCALE
    )

    if image is None:
        return 0, 0

    # Dark pixel dianggap foreground
    _, binary = cv2.threshold(
        image,
        127,
        255,
        cv2.THRESH_BINARY_INV
    )

    foreground = np.sum(
        binary == 255
    )

    total = binary.shape[0] * binary.shape[1]

    persentase = (
        foreground / total
    ) * 100

    return foreground, persentase


# ==========================================================
# AMBIL FILE
# ==========================================================
present_files = sorted(
    glob.glob(
        os.path.join(
            PRESENT_FOLDER,
            "*.jpg"
        )
    )
)

absent_files = sorted(
    glob.glob(
        os.path.join(
            ABSENT_FOLDER,
            "*.jpg"
        )
    )
)


# ==========================================================
# HEADER
# ==========================================================
print()
print("=" * 95)
print("TABEL HASIL DETEKSI TANDA TANGAN")
print("=" * 95)

print(
    f"{'No':<4}"
    f"{'Dataset':<10}"
    f"{'Nama File':<35}"
    f"{'Foreground':>15}"
    f"{'Persentase':>13}"
    f"{'Hasil':<20}"
)

print("-" * 95)


# ==========================================================
# DATA HASIL
# ==========================================================
hasil_semua = []

nomor = 1


# ==========================================================
# PRESENT
# ==========================================================
for path in present_files:

    foreground, persentase = hitung_foreground(path)

    if foreground >= BATAS:
        hasil = "SIGNATURE PRESENT"
    else:
        hasil = "SIGNATURE ABSENT"

    hasil_semua.append(
        [
            nomor,
            "PRESENT",
            os.path.basename(path),
            foreground,
            persentase,
            hasil
        ]
    )

    nomor += 1


# ==========================================================
# ABSENT
# ==========================================================
for path in absent_files:

    foreground, persentase = hitung_foreground(path)

    if foreground >= BATAS:
        hasil = "SIGNATURE PRESENT"
    else:
        hasil = "SIGNATURE ABSENT"

    hasil_semua.append(
        [
            nomor,
            "ABSENT",
            os.path.basename(path),
            foreground,
            persentase,
            hasil
        ]
    )

    nomor += 1


# ==========================================================
# TAMPILKAN TABEL
# ==========================================================
for data in hasil_semua:

    print(
        f"{data[0]:<4}"
        f"{data[1]:<10}"
        f"{data[2]:<35}"
        f"{data[3]:>15}"
        f"{data[4]:>12.2f}% "
        f"{data[5]:<20}"
    )


# ==========================================================
# HITUNG AKURASI
# ==========================================================
benar = 0

for data in hasil_semua:

    kondisi_sebenarnya = data[1]
    hasil_program = data[5]

    if kondisi_sebenarnya == "PRESENT":
        if hasil_program == "SIGNATURE PRESENT":
            benar += 1

    elif kondisi_sebenarnya == "ABSENT":
        if hasil_program == "SIGNATURE ABSENT":
            benar += 1


total_data = len(hasil_semua)

if total_data > 0:
    akurasi = (
        benar / total_data
    ) * 100
else:
    akurasi = 0


# ==========================================================
# RINGKASAN
# ==========================================================
print()
print("=" * 95)
print("RINGKASAN")
print("=" * 95)

print(f"Jumlah data PRESENT : {len(present_files)}")
print(f"Jumlah data ABSENT  : {len(absent_files)}")
print(f"Total data          : {total_data}")
print(f"Data benar          : {benar}")
print(f"Data salah          : {total_data - benar}")
print(f"Akurasi             : {akurasi:.2f}%")
print(f"Batas klasifikasi   : {BATAS:.2f}")

print("=" * 95)


# ==========================================================
# SIMPAN HASIL KE TXT
# ==========================================================
with open(
    "hasil_tabel_18_data.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "TABEL HASIL DETEKSI TANDA TANGAN\n"
    )

    file.write("=" * 95 + "\n")

    for data in hasil_semua:

        file.write(
            f"{data[0]:<4}"
            f"{data[1]:<10}"
            f"{data[2]:<35}"
            f"{data[3]:>15}"
            f"{data[4]:>12.2f}% "
            f"{data[5]:<20}\n"
        )

    file.write("\n")
    file.write("RINGKASAN\n")
    file.write("=" * 95 + "\n")

    file.write(
        f"Jumlah data PRESENT : {len(present_files)}\n"
    )

    file.write(
        f"Jumlah data ABSENT  : {len(absent_files)}\n"
    )

    file.write(
        f"Total data          : {total_data}\n"
    )

    file.write(
        f"Data benar          : {benar}\n"
    )

    file.write(
        f"Data salah          : {total_data - benar}\n"
    )

    file.write(
        f"Akurasi             : {akurasi:.2f}%\n"
    )

    file.write(
        f"Batas klasifikasi   : {BATAS:.2f}\n"
    )

print()
print("File hasil disimpan sebagai:")
print("hasil_tabel_18_data.txt")