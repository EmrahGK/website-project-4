import time


while True:
    ad = input("\n\nadınızı giriniz: ")
    soyad = input("soyadınızı giriniz: ")
    yaş = input("yaşınızı giriniz: ")


    if(ad == "q" or  soyad == "q" or yaş == "q"):
        time.sleep(0.5)
        break 

    try:
        yaş = int(yaş)
    except:
        print(f"{ad} {soyad}; Yanlış bir değer girdiniz.")
        time.sleep(0.5)
        continue

    if(yaş > 18):
        print(f"{ad} {soyad}; 18'den büyüksünüz. ({yaş})")
        time.sleep(0.5)
        continue
    elif(yaş < 18):
        print(f"{ad} {soyad}; 18 yaşından küçüksünüz. Site politikalarımız içeri girmenize izin vermemektedir xd({yaş})")
        time.sleep(0.5)
        continue
    else:
        print(f"{ad} {soyad}; Yanlış bir değer girdiniz. Değer ({yaş}) olamaz.")
        time.sleep(0.5)
        continue

        