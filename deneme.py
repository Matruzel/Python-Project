kume1 = set([2,6,7,8,12,13,14,16])
kume2 = set([3,6,9,10,12,13,15,16])
kume3 = set([4,7,9,11,12,14,15,16])
kume4 = set([5,8,10,11,13,14,15,16])

sonuc = set()

giris = (""" 

1 ve 16 arasında (1-16 dahil) aklınızdan bir sayı tutunuz.
Sayınızın olduğu kümelere (+) koyunuz olmayanlarada (-) koyunuz.
Örnek: 1 kümesinde var [1]->> +   yanına (+) yazıcağım
       2 kümesinde yok [2]->> -   yanına (-) yazıcağım

----------------------------
| 1- 2/6/7/8/12/13/14/16   |     
| 2- 3/6/9/10/12/13/15/16  | 
| 3- 4/7/9/11/12/14/15/16  |
| 4- 5/8/10/11/13/14/15/16 |
----------------------------

""")

print(giris)

x1 = input("[1]->> ")
x2 = input("[2]->> ")
x3 = input("[3]->> ")
x4 = input("[4]->> ")

if x1 == str("+"):
    if len(sonuc) == 0:
        sonuc.symmetric_difference_update(kume1)
    else:
        sonuc.intersection_update(kume1)

if x2 == str("+"):
    if len(sonuc) == 0:
        sonuc.symmetric_difference_update(kume2)
    else:
        sonuc.intersection_update(kume2)

if x3 == str("+"):
    if len(sonuc) == 0:
        sonuc.symmetric_difference_update(kume3)
    else:
        sonuc.intersection_update(kume3)

if x4 == str("+"):
    if len(sonuc) == 0:
        sonuc.symmetric_difference_update(kume4)
    else:
        sonuc.intersection_update(kume4)

if x1 == str("-"):
    sonuc.difference_update(kume1)

if x2 == str("-"):
    sonuc.difference_update(kume2)

if x3 == str("-"):
    sonuc.difference_update(kume3)

if x4 == str("-"):
    sonuc.difference_update(kume4)

print(sonuc)

k = input("Programdan çıkmak için enter'a basın.")



