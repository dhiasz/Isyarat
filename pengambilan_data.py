import cv2
import os
import time

# -------------------------------
# PENGATURAN AWAL
# -------------------------------

label = 0  # 0 = A
jumlah_gambar = 100
folder = "dataset"

path_kelas = os.path.join(folder, str(label))
os.makedirs(path_kelas, exist_ok=True)

# -------------------------------
# AKSES KAMERA
# -------------------------------

kamera = cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # penting agar tidak lag

jumlah_tersimpan = 0
waktu_terakhir_simpan = 0
delay_simpan = 0.3  # 300 ms antar simpan

# -------------------------------
# LOOP PENGAMBILAN GAMBAR
# -------------------------------

while True:
    ret, frame = kamera.read()
    if not ret:
        print("Gagal Mengakses Kamera")
        break

    cv2.putText(
        frame,
        "Tekan 'S' : Simpan | 'Q' : Keluar",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Jumlah tersimpan: {jumlah_tersimpan}/{jumlah_gambar}",
        (10, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.imshow("Pengambilan Data Gesture", frame)

    tombol = cv2.waitKey(1) & 0xFF
    waktu_sekarang = time.time()

    if tombol == ord('s'):
        if waktu_sekarang - waktu_terakhir_simpan > delay_simpan:
            nama_file = f"{jumlah_tersimpan}.jpg"
            path_file = os.path.join(path_kelas, nama_file)

            cv2.imwrite(path_file, frame)
            jumlah_tersimpan += 1
            waktu_terakhir_simpan = waktu_sekarang

            print(f"Gambar disimpan: {path_file}")

    if jumlah_tersimpan >= jumlah_gambar:
        print("Pengambilan data selesai")
        break

    if tombol == ord('q'):
        print("Pengambilan data dihentikan")
        break

# -------------------------------
# BERSIHKAN RESOURCE
# -------------------------------

kamera.release()
cv2.destroyAllWindows()
  