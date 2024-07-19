# Hangman Oyunu

Bu proje, klasik Hangman (Adam Asmaca) oyununu Python dilinde basit bir komut satırı uygulaması olarak implement eder. Oyunda, rastgele seçilen bir kelimeyi tahmin etmeye çalışırsınız. Her yanlış tahminde, bir "adam" resmi çizilir ve tahmin haklarınız azalır.

## Özellikler

- **Rastgele Kelime Seçimi:** `kelimeler` adlı bir liste içinden rastgele bir kelime seçilir.
- **Harf Tahmini:** Tek bir harf tahmini yapılabilir. Kullanıcı sadece harf girme zorunluluğuna sahiptir.
- **Geri Bildirim:** Kullanıcı doğru tahminler yaptıkça, doğru tahmin edilen harfler ekranda gösterilir.
- **Yanlış Tahminler:** Yanlış tahminler için bir çizim (adam resmi) gösterilir.
- **Oyun Sonu:** Tahmin hakkı bittiğinde veya tüm harfler tahmin edildiğinde oyun sona erer.

## Gereksinimler

- `colorama`: Terminal renkleri için kütüphane. [colorama PyPI](https://pypi.org/project/colorama/)
- `random`: Python'un standart kütüphanesi.

## Kurulum

1. Python'un bilgisayarınızda kurulu olduğundan emin olun.
2. `colorama` kütüphanesini yüklemek için terminal veya komut istemcisine şu komutu yazın:
   ```bash
   pip install colorama
