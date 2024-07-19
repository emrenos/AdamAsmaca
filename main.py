import random
from aa_kelimeler import kelimeler
from aa_logo import logo
from aa_parcalar import parcalar
from colorama import Fore, Style, init

init(autoreset=True)

BOLD = '\033[1m'
RESET = '\033[0m'

secilen_kelime = random.choice(kelimeler)
dogru_tahminler = set()
bosluk = len(secilen_kelime)
deneme_hakki = 6

print(logo)
print(" ".join("_" for _ in range(bosluk)))

while deneme_hakki > 0:
    tahmin = input(f"{Fore.YELLOW}{BOLD}Bir harf tahmin edin: {RESET}{Style.RESET_ALL}").lower()

    while not tahmin.isalpha():
        tahmin = input(f"{Fore.RED}{BOLD}Lütfen sadece harf girin: {RESET}{Style.RESET_ALL}").lower()
    while not len(tahmin) == 1:
        tahmin = input(f"{Fore.RED}{BOLD}Lütfen sadece tek harf girin: {RESET}{Style.RESET_ALL}").lower()

    if tahmin in secilen_kelime and tahmin not in dogru_tahminler:
        dogru_tahminler.add(tahmin)

    dogru_tahmin_sayisi = 0
    for harf in secilen_kelime:
        if harf in dogru_tahminler:
            print(f"{Fore.GREEN}{BOLD}{harf}{RESET}{Style.RESET_ALL}", end=" ")
            dogru_tahmin_sayisi += 1
        else:
            print("_", end=" ")
    print()

    if tahmin not in dogru_tahminler:
        deneme_hakki -= 1
        print(parcalar[deneme_hakki])
        if deneme_hakki == 0:
            print(f"{Fore.RED}{BOLD}Tahmin hakkınız bitti. Tahmin etmeniz gereken kelime:{RESET} {secilen_kelime}{Style.RESET_ALL}")
            break

    if dogru_tahmin_sayisi == bosluk:
        print(f"{Fore.GREEN}{secilen_kelime}{BOLD} kelimesini doğru tahmin ettiniz!{RESET}{Style.RESET_ALL}")
        break
