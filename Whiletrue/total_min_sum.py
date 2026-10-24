total = 0
count = 0
numbers = []

while True:
    text = input("Enter a number or stop: ")

    if text == "stop":
        break

    try:
        num = float(text)
        total = total + num
        count = count + 1
        numbers.append(num)

    except:
        print("გთხოვთ შეიყვანოთ მარტო რიცხვი ან 'stop' ")

print("Total:", total)
print("Count:", count)

if count > 0:
    print("Max:", max(numbers))
    print("Min:", min(numbers))