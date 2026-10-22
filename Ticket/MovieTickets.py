import re 

text = input("შეიყვანეთ ჯავშნის ინფორმაცია: ")

try:
    numbers = re.findall(r"\d+(?:\.\d+)?", text)

    tickets = int(numbers[0])
    paid_money = float(numbers[1])

    total_price = tickets * 15

    if tickets <= 0:
        raise ValueError("ბილეთების რაოდენობა უნდა იყოს მინიმუმ 1")

    if paid_money < total_price:
        raise ValueError("თანხა არ არის საკმარისი")

except IndexError:
    print("შეცდომა: ტექსტში საკმარისი რიცხვები არ არის.")

except ValueError as error:
    print("შეცდომა:", error)

else:
    change = paid_money - total_price

    print("\n--- ჯავშნის ინფორმაცია ---")
    print(f"ბილეთების რაოდენობა: {tickets}")
    print(f"ერთი ბილეთის ფასი: 15 ლარი")
    print(f"ჯამური ღირებულება: {total_price:.2f} ლარი")
    print(f"გადახდილი თანხა: {paid_money:.2f} ლარი")
    print(f"ხურდა: {change:.2f} ლარი")
    print("ჯავშანი წარმატებით შესრულდა!")

finally:
    print("[სისტემა]: ტრანზაქციის მცდელობა დასრულდა.")




