# 1. while istifadə edərək listin məlumatlarını çap edin.
fruits=['alma','nar','heyva','uzum','gilas']
num=0
while num<len(fruits):
    print(fruits[num])
    num+=1

# 2. Hərflərdən ibarət list yaradın. While və continue istifadə edərək bəzi hərflərin üzərindən keçərək digər hərfləri çap edin
letters=['a','b','c','d','f','e','g']
choies=(input("Herf daxil edin :"))
num=0
while num<len(letters):
    if letters[num]==choies:
        num+=1
        continue
        
    print(letters[num])
    num+=1




# 3.  while istifadə edərək Sıfırdan daxil edilmiş ədədə qədər(ədəd daxil olmaqla) çap edin
number=int(input("Bir eded daxil edin :"))
num=0
while num<=number:
    print(num)
    num+=1



# 4. Static bir password yaradin. Daxil edilen parolun 3 dəfə səhv yazılma şansı olsun və hər səhv yazıldıqda 1 şansınız azaldı mesajı versin. Əgər şanslar bitərsə block olundunuz mesajı verilsin. For-dan istifadə edin
error=3
password="abscdf1235"

for x in range(3):
    choies=input("Parolu daxil edin :")
    if choies!=password:
        error-=1
        print(f'Parol duz gun deyil {error} sansiniz qaldi')
    elif error==0:
        
        break
    else:
        print("siz dogru cavabi bildiniz")


# 5. Test sistemi yaradin. Doğru və yanlış sualların sayını hesablasın. Əlavə olaraq 4 səhv 1 düz cavabı silib son nəticəni çap edin


sual1=input("""
1)	Albaniyada kirəmit istehsali nəyin təsiri nəticəsində yaranmişdir?	

A)	Yunan mədəniyyətinin
B)	Midiya mədəniyyətinin
C)	Roma mədəniyyətinin
D)	Aşşur mədəniyyətinin

 cavab  :""")

sual2=input("""
2)	1902 - ci ildə Şəki rayonunun Böyük Dəhnə kəndində tapilmişdir:	

A)	Katakomba qəbirləri
B)	Müxtəlif tikinti qaliqlari
C)	Üzərində yunan dilində yazi olan daş
D)	Herakla məxsus məbəd

 cavab  :""")

sual3=input("""
3)	Albaniyanin dini nə olmuşdur?

A)	Çoxallahliliq
B)	Zərdüştlük
C)	Şamançiliq
D)	Bütpərəstlik

 cavab  :""")


sual4=input("""
4)Azərbaycan dilində neçə sait var?

A)	10
B)	3
C)	2
D)	5
E)	9

 cavab  :""")


sual5=input("""
5)	Albaniyanin Zevs ( Göy ), Helios ( Günəş ), Selena ( Ay ) allahlarina sitayiş etmələri barədə məlumat vermiş antik müəllif:	
A)	Appian
B)	Kanidi
C)	Ptolomey
D)	Strabon

 cavab :""")

query={
    "sual1":sual1,
    "sual2":sual2,
    "sual3":sual3,
    "sual4":sual4,
    "sual5":sual5
}
answer={
    "sual1":"a",
    "sual2":"b",
    "sual3":"c",
    "sual4":"d",
    "sual5":"a"
}
true1=0
error=0
for key,value in query.items():
   if value==answer[key]:
      true1+=1
      print(f"Cavabiniz duzgundur. Dogru cavab sayi :{true1}")

   else:
      error+=1
      print(" Cavab sehvdir.")
      if error==4:
         true1-=1
print(f'Dogru cavab sayi :{true1}')