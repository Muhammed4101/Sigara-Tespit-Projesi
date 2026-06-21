# Sigara-Tespit-Projesi

# 🚭 Akıllı Güvenlik ve Real-Time Sigara İhlal Tespit Sistemi

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8_Nano-orange.svg)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)

Kapalı alanlar, okul koridorları ve yangın çıkışlarında güvenliği sağlamak amacıyla geliştirilmiş, **donanım optimizasyonlu** ve **uçtan uca (End-to-End)** çalışan gerçek zamanlı bir bilgisayarlı görü (Computer Vision) projesidir. Sistem, yerel donanımları yormadan 7/24 izleme yapar ve ihlal anında yetkililere görsel kanıtlı bildirim gönderir.

---

## 🚀 Öne Çıkan Özellikler

* **Veri Seti Optimizasyonu (v18):** Roboflow üzerinde veri artırma (Augmentation) teknikleri kullanılarak ham veri seti **3.000+ zenginleştirilmiş görsele** ulaştırılmış ve zorlu ışık/açı koşullarında **%89 mAP50** doğruluğu yakalanmıştır.
* **7/24 Donanım Optimizasyonu:** Geliştirilen **Kare Atlama (Frame Skipping)** algoritması sayesinde işlemci (CPU) yükü **%80 azaltılmış**, sistemin standart ofis bilgisayarlarında bile ısınmadan ve çökmeden çalışması sağlanmıştır.
* **Akıllı Bildirim Entegrasyonu:** Model bir ihlal tespit ettiği anda otomatik olarak o karenin anlık görüntüsünü (snapshot) alır ve tarih ve saat bilgileriyle klasöre kaydeder.
* **Dinamik Bağlantı Yönetimi:** Kamera veya IP yayın akışında kopma yaşandığında sistem kilitlenmez; otomatik olarak yeniden bağlanmayı dener.

---

## 🛠️ Kullanılan Teknolojiler

* **Geliştirme Dili:** Python
* **Model Mimarisi:** YOLOv8 (Nano - Edge cihazlar ve hafif donanımlar için optimize)
* **Görüntü İşleme:** OpenCV (Video/Kamera Stream Yönetimi)
* **Veri Yönetimi:** Roboflow Universe


---

## 📂 Proje Yapısı

```text
│   └── best.pt              # Eğitilmiş ve optimize edilmiş YOLOv8 model ağırlığı
│   ├── kamera_test.py       # Canlı kamera ve IP kamera takip scripti
