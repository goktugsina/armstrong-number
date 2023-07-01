print("""
★★★★★★★★★★★★★★★★

Armstrong Sayısı Bulma

Armstrong Sayısı: 
Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan 
her birinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse 
bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

★★★★★★★★★★★★★★★★
""")

sayi = input("Bir Sayı Giriniz:")
toplam = 0
basamak = len(sayi)


for i in sayi:
    i = int(i)
    i = i**basamak
    toplam += i
    print(toplam)

sayi = int(sayi)

if toplam == sayi:
    print("Bu sayı bir Armstrong Sayısıdır!")
else:
    print("Bu sayı bir Armstrong Sayısı Değildir!")
