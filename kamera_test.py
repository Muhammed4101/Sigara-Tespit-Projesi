import cv2
import os
from ultralytics import YOLO
import datetime
import time  # Saniye kontrolü için eklendi

# 1. Eğitilmiş YOLO modelini yükle
model_path = 'best.pt' 
model = YOLO(model_path)

# 2. Kaydedilecek ekran görüntüleri için bir klasör oluştur
save_dir = 'detected_cigarette_screenshots'
os.makedirs(save_dir, exist_ok=True)

print(f"[BİLGİ] Tespit edilen ekran görüntüleri şuraya kaydedilecek: {save_dir}")

# 3. Video veya Kamera akışını başlat (0 yerine video yolu da yazabilirsiniz)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kaynak açılamadı.")
    exit()

print("Akış başlatıldı. Sigara tespit edildiğinde saniyede en fazla 1 ekran görüntüsü kaydedilecek. Çıkmak için 'q' tuşuna basın...")

saved_screenshot_count = 0
last_save_time = 0  # Son fotoğraf kaydetme zamanını tutan değişken

while True:
    ret, frame = cap.read()

    if not ret:
        print("Kare okunamadı veya video bitti, çıkılıyor...")
        break

    # YOLO modelini kullanarak kare üzerinde tahmin yap
    results = model.predict(source=frame, show=False, conf=0.5, save=False, verbose=False)

    # Tespit var mı kontrol et
    if len(results[0].boxes) > 0:
        annotated_frame = results[0].plot() 
        current_time = time.time()  # Şu anki zamanı saniye cinsinden al

        # KRİTİK NOKTA: Son kayıttan sonra 1 saniye geçti mi?
        if current_time - last_save_time >= 1.0:
            # Kaydedilecek dosya adını oluştur
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(save_dir, f"detected_cigarette_{timestamp}.jpg")

            # Görüntüyü kaydet
            cv2.imwrite(save_path, annotated_frame)
            saved_screenshot_count += 1
            print(f"[KAYDEDİLDİ] Sigara tespit edildi ({saved_screenshot_count}. resim): {save_path}")
            
            # Son kaydetme zamanını güncelle
            last_save_time = current_time

        # Tespit anını ekranda canlı göster
        cv2.imshow('YOLO Canlı Tespit', annotated_frame)

    else:
        # Tespit yoksa orijinal kareyi göster
        cv2.imshow('YOLO Canlı Tespit', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\n'q' tuşuna basıldı, çıkılıyor...")
        break

cap.release()
cv2.destroyAllWindows()

print(f"[BİLGİ] Toplamda {saved_screenshot_count} adet ekran görüntüsü kaydedildi: {save_dir}")
