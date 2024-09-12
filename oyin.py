import random

print("Salom, o'yinga xush kelibsiz!")
print("Bu o'ylangan sonni taxmin etish oyini.")
print("Sizda 7 ta shans bor. Keling o'yinni boshlaymiz!")

# 0 dan 99 gacha biror sonni
# generate qilib olamiz
oylangan_son = random.randrange(100)

shanslar = 7

taxminlar_soni = 0

while taxminlar_soni < shanslar:

    taxminlar_soni += 1
    foydalanuvchi_taxmini = int(input("Iltimos taxminingizni kiriting: "))

    if foydalanuvchi_taxmini == oylangan_son:
        print(
            f"O'ylangan son {oylangan_son} edi va siz uni {taxminlar_soni} ta harakatda topdingiz!"
        )
        break

    elif taxminlar_soni >= shanslar and foydalanuvchi_taxmini != oylangan_son:
        print(
            f"Oops uzr, o'ylangan son {oylangan_son} edi. Keyingi safarga omad tilayman!"
        )

    elif foydalanuvchi_taxmini > oylangan_son:
        print("Taxminingiz o'ylangan sondan katta, kichikroq son kiriting!")

    elif foydalanuvchi_taxmini < oylangan_son:
        print("Taxminingiz o'ylangan sondan kichik, kattaroq son kiriting")
