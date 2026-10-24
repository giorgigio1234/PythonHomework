while True:
    try:
        height = int(input("შეეიყვანეთ სიმაღლე (1-8): "))

        if 1 <= height <= 8:
            break
        else:
            print("შეიყვანეთ რიცხვი 1-დან 8-ის ჩათვლით.")

    except ValueError:
        print("გთხოვთ შეიყვანოთ მთელი რიცხვი.")


for i in range(1, height + 1):
    for j in range(height - i):
        print("", end="")

    for j in range(i):
        print("#", end="")

    print("")
