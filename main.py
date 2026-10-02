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
# FUNGSI ANALISIS
# ==========================================================
def analisis_gambar(path):

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        return 0, 0, 0

    # Pastikan gambar biner
    _, binary = cv2.threshold(
    image,
    127,
    255,
    cv2.THRESH_BINARY_INV
)

    # Hitung foreground
    foreground = np.sum(binary == 255)

    total_pixel = binary.shape[0] * binary.shape[1]

    persentase = (
        foreground / total_pixel
    ) * 100

    return foreground, total_pixel, persentase


# ==========================================================
# BACA DATASET PRESENT
# ==========================================================
present_files = sorted(
    glob.glob(
        os.path.join(PRESENT_FOLDER, "*.jpg")
    )
)

# ==========================================================
# BACA DATASET ABSENT
# ==========================================================
absent_files = sorted(
    glob.glob(
        os.path.join(ABSENT_FOLDER, "*.jpg")
    )
)

print("=" * 70)
print("DETEKSI KEBERADAAN TANDA TANGAN")
print("=" * 70)

print()
print("Jumlah PRESENT :", len(present_files))
print("Jumlah ABSENT  :", len(absent_files))


# ==========================================================
# ANALISIS PRESENT
# ==========================================================
print()
print("=" * 70)
print("DATASET PRESENT")
print("=" * 70)

present_values = []

for i, path in enumerate(present_files, start=1):

    foreground, total, percentage = analisis_gambar(path)

    present_values.append(foreground)

    print(
        f"{i:02d}. {os.path.basename(path)}"
    )
    print(
        f"    Foreground : {foreground}"
    )
    print(
        f"    Persentase : {percentage:.2f}%"
    )


# ==========================================================
# ANALISIS ABSENT
# ==========================================================
print()
print("=" * 70)
print("DATASET ABSENT")
print("=" * 70)

absent_values = []

for i, path in enumerate(absent_files, start=1):

    foreground, total, percentage = analisis_gambar(path)

    absent_values.append(foreground)

    print(
        f"{i:02d}. {os.path.basename(path)}"
    )
    print(
        f"    Foreground : {foreground}"
    )
    print(
        f"    Persentase : {percentage:.2f}%"
    )


# ==========================================================
# HITUNG RATA-RATA
# ==========================================================
present_average = np.mean(present_values)
absent_average = np.mean(absent_values)

print()
print("=" * 70)
print("RATA-RATA FOREGROUND")
print("=" * 70)

print(
    f"Rata-rata PRESENT : {present_average:.2f}"
)

print(
    f"Rata-rata ABSENT  : {absent_average:.2f}"
)


# ==========================================================
# THRESHOLD / BATAS
# ==========================================================
threshold = (
    present_average + absent_average
) / 2

print()
print("=" * 70)
print("ATURAN KLASIFIKASI")
print("=" * 70)

print(
    f"Nilai batas (threshold) : {threshold:.2f}"
)

print()
print("Jika foreground >= threshold")
print("        -> SIGNATURE PRESENT")

print()
print("Jika foreground < threshold")
print("        -> SIGNATURE ABSENT")


# ==========================================================
# UJI PRESENT
# ==========================================================
print()
print("=" * 70)
print("HASIL KLASIFIKASI PRESENT")
print("=" * 70)

for i, value in enumerate(present_values, start=1):

    if value >= threshold:
        hasil = "SIGNATURE PRESENT"
    else:
        hasil = "SIGNATURE ABSENT"

    print(
        f"Present {i:02d} : {value} -> {hasil}"
    )


# ==========================================================
# UJI ABSENT
# ==========================================================
print()
print("=" * 70)
print("HASIL KLASIFIKASI ABSENT")
print("=" * 70)

for i, value in enumerate(absent_values, start=1):

    if value >= threshold:
        hasil = "SIGNATURE PRESENT"
    else:
        hasil = "SIGNATURE ABSENT"

    print(
        f"Absent {i:02d} : {value} -> {hasil}"
    )


# ==========================================================
# SELESAI
# ==========================================================
print()
print("=" * 70)
print("ANALISIS SELESAI")
print("=" * 70)