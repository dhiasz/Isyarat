import os
import cv2
import pickle
import mediapipe as mp

# Inisialisasi tangan menggunakan MediaPipe tangan
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
)

# Ini Bagian folder dataset

DATASET_DIR = "dataset"

data = []
labels = []

print("Memulai pembuatan dataset...")

#looping setiap folder 
for label in sorted(os.listdir(DATASET_DIR)):
    folder_path = os.path.join(DATASET_DIR, label)
    
    if not os.path.join(folder_path):
        continue
    
    print(f"Memproses folder {label}")
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Membaca Gambar
        img = cv2.imread(file_path)
        if img is None:
            continue
        
        # Ubah ke RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Deteksi tangan
        result = hands.process(img_rgb)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                fitur = []
                
                for titik in hand_landmarks.landmark:
                    fitur.append(titik.x)
                    fitur.append(titik.y)
                    
                data.append(fitur)
                labels.append(int(labels))
                

print("Total data : ", len(data))
print("Total label : ", len(labels))
                    
    
 #simpan file
with open("Dataset.pickle", "wb") as f:
     pickle.dump({"data" : data, "label": labels}, f)
     
print("Dataset berhasil dibuat dan disimpan sebagai dataset.pickle")