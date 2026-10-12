print("შეიყვანეთ თქვენი სახელი:")
name = input()

print("შეიყვანეთ თქვენი გვარი:")
surname = input()

print("შეიყვანეთ თქვენი დაბადების წელი:")
birthyear = int(input())

print("შეიყვანეთ თქვენი საყვარელი პროგრამირების ენა:")
programmingLang = input()

print("სახელი", name.upper(), "გვარი", surname.upper(), "ასაკი:", birthyear, "პროგრამირების ენა:", programmingLang.upper(), sep=" | ")

weli = 2026 - birthyear

adult = birthyear >= 18

score = int(input("შეიყვანეთ მიღებული ქულა (მაქსიმუმ 20 ქულა): "))
grade = score // 2

print("თქვენი ნიშანია: ",grade)