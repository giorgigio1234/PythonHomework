print("შეიყვანეთ თქვენი სახელი: ")
firstname = input()

print("შეიყვანეთ თქვენი გვარი: ")
lastname = input()

print("აირჩიეთ თქვენი პლათფორმა: (მაგ: gmail.com, itstep.ge, yahoo.com)")
platform = input()

firstname = firstname.strip().lower()
lastname = lastname.strip().lower()
platform = platform.strip().lower()

first_two = firstname[:2]
email = f"{first_two}{lastname}@{platform}"

print(f"\nგენერირებული ელფოსტა: {email}")
print()
print("თქვენი ელფოსტა შეიქმნა")

