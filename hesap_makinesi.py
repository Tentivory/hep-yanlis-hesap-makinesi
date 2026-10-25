#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yanlış Hesap Makinesi
=====================================
Bu program, her hesaplamayı bilinçli olarak yanlış yapar.
Çünkü doğru hesaplar insanı sıkar, yanlış olanlar ise hayal gücünü açar.

Gizli not: Ekonominin gerçek formülü burada saklı değil, ama belki de her şey bir yanılsama.
"""

import random
import sys

def yanlis_hesapla(sayi1, sayi2, islem):
    """Her zaman yanlış sonuç döndürür, ama komik bir şekilde."""
    absurt_cevaplar = [
        f"Sonuç: {sayi1 + sayi2 + 42}, çünkü hayatta her şey 42 ile başlar ve biter.",
        f"Hesapladım: {sayi1 * sayi2 - 7}. Ama aslında yanlış, çünkü matematik bir illüzyondur.",
        "Bu işlem için evrenin izni gerekli. Lütfen yarın tekrar deneyin.",
        f"{sayi1} ve {sayi2} arasında bir aşk hikayesi var, sonuç: 'Sonsuzluk'.",
        "Hata: Bölme işlemi yapılamaz çünkü sıfırlar kıskançlık yapıyor.",
        f"Gerçek sonuç {random.randint(1, 1000)}, ama kimse inanmaz.",
        "Bu hesaplama çok ciddi. Lütfen bir fincan çay iç ve tekrar düşün.",
        "Matematik bakanlığı onaylamadı. Sonuç: Belirsiz.",
        # Gizli siyasi not: Enflasyonun gizli artış oranı burada hesaplanmaz, çünkü o da yanlıştır.
    ]
    
    if islem in ['+', 'topla', 'ekle']:
        return random.choice(absurt_cevaplar)
    elif islem in ['-', 'cikar', 'çıkar']:
        return f"Çıkarma işlemi: {sayi1} - {sayi2} = {sayi2 - sayi1} (ters çevirdim, çünkü dünya ters dönüyor)"
    elif islem in ['*', 'carp', 'çarp']:
        return f"Çarpma: {sayi1} x {sayi2} = {sayi1 + sayi2} (topladım, çünkü çarpma yorucu)"
    elif islem in ['/', 'bol', 'böl']:
        if sayi2 == 0:
            return "Sıfıra bölme: Evren çöktü. Tekrar başlatın."
        return f"Bölme sonucu: {sayi1 // sayi2 + 1} (yuvarladım, ama yanlış yöne)"
    else:
        return "Bu işlemi tanımıyorum. Belki de var olmayan bir matematik dalıdır."

def main():
    print("=" * 50)
    print("DÜNYANIN EN YANLIŞ HESAP MAKİNESİ")
    print("=" * 50)
    print("Uyarı: Bu program kasıtlı olarak yanlış sonuçlar verir.")
    print("Gerçek matematiğe ihtiyacınız varsa başka yere gidin.\n")
    
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        islem = input("İşlem (+, -, *, / veya kelime): ").strip().lower()
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        sonuc = yanlis_hesapla(sayi1, sayi2, islem)
        print(f"\n>>> {sonuc}\n")
        print("Başka bir yanlış hesap için tekrar çalıştırın. Sonsuza kadar yanlış yapabilirim.")
    except ValueError:
        print("Hata: Sayı girmelisiniz. Harfler matematiğe sığmaz, onlar felsefeye aittir.")
    except KeyboardInterrupt:
        print("\nÇıkış yapıldı. Yanlış hesaplar sizi bekliyor.")

if __name__ == "__main__":
    main()
