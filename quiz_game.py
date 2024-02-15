import time


print("Quiz oyununa hoş geldiniz!")

playing = input("Oynamak istiyor musunuz? (y/n)\n").lower()

if playing != "y":
    quit()

print("Oyun başlıyor...")
score = 0
time.sleep(5)

answer = input("CPU'nun açılımı nedir? \n\ncentral processing unit \ncentral palindrom united \ncontinuos processing unit \n\n").lower()
if answer == "central processing unit":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")
time.sleep(5)

answer = input("Hazırladığınız kodlar bilgisayarın hangi biriminde saklanır? \n\nrastgele erişimli hafıza \nsabit disk \ngrafik işlemci birimi \n\n").lower()
if answer == "sabit disk":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")
time.sleep(5)

answer = input("Çoğu web sitesi hangi tür kodlamayı kullanır? \n\nUTF-32 \nUTF-8 \nUTF-16 \n\n")
if answer == "UTF-8":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")
time.sleep(5)

answer = input("Grafik işlem biriminin ingilizce kısaltması nedir? \n\nCPU \nRAM \nGPU \n\n")
if answer == "GPU":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")
time.sleep(5)

answer = input("Hangi değişken türü ondalıklı sayıları içerir? \n\ndouble \ninteger \nboolean \n\n").lower()
if answer == "double":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")
time.sleep(5)

answer = input("HTML dilinde hazırlananbir projede, sayfada bir bölüm ya da boş bir kutu oluşturulmak için hangi etiket kullanılır? \n\n<body> \n<textarea> \n<div> \n\n").lower()
if answer == "<div>":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")
time.sleep(5)

answer = input("Bir ya da daha fazla işlemi yapan en basit kod bloğuna ne denir? \n\nsınıf \nmodül \nfonksiyon \n\n").lower()
if answer == "fonksiyon":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")
time.sleep(5)

answer = input("Programlamayı kimler öğrenmelidir? \n\nöğrenciler \nyazılımcılar \nherkes \n\n").lower()
if answer == "herkes":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")
time.sleep(5)

answer = input('HTML dilinde `<div class="kare"></div>` bölmesini CSS dilinde hangi seçici kullanılarak stilize ederiz? \n\n.kare \n#kare \ndiv > kare \n\n').lower()
if answer == ".kare":
    print("Doğru!")
    score += 1
else:
    print("Yanlış :(")

print("Sıradaki soru...")


print("Skor hesaplanıyor...")
time.sleep(2.5)
print("Toplamda " + str(score) + " skor aldınız!")