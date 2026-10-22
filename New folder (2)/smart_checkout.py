cart_total = float(input("შეიყვანეთ კალათის ფასი: "))
user_status = input("შეიყვანე სტატუსი (regular, vip, admin): ")
has_promocode = input("გაქვს პრომოკოდი? (yes/no): ")
loyalty_points = input("შეიყვანე დაგროვილი ქულები: ")
deliverycity = input("შეიყვანეთ ქალაქი: ")
is_account_active = input("აქტიურია ანგარიში? (yes/no): ")

if is_account_active == "no":
    print("ანგარიში დაბლოკილია, შეკვეთა ვერ დამუშავდება")

elif cart_total <= 0:
    print("შეცდომა: კალათის ფასი უნდა იყოს 0-ზე მეტი.")


else:
    discount = 0

    if user_status == "vip":
        if loyalty_points >= 500:
            discount = 25
        else:
            discount = 20

    elif user_status == "admin":
        discount = 50

    discount_price = cart_total - (cart_total * discount / 100)


    if deliverycity in ["თბილისი","ქუთაისი","ბათუმი"]:
        if discount_price >= 100:
            delivery_prize = 0
        else:
            delivery_prize = 5
    else: 
        delivery_prize = 15


    final_price = discount_price + delivery_prize

    print("\n--- შეკვეთის ინვოისი ---")
    print("საწყისი ფასი:", cart_total, "ლარი")
    print("ფასდაკლება:", discount, "%")
    print("ფასდაკლებული ფასი:", round(discount_price, 2), "ლარი")
    print("მიტანის საფასური:", delivery_prize, "ლარი")
    print("საბოლოო გადასახდელი:", round(final_price, 2), "ლარი")

        

