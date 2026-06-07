total = 0

while True:
    expense = input("Enter expense or done: ")

    if expense == "done":
        break

    try:
        total += float(expense)
    except:
        print("Please enter a number.")

print("Total Spent =", total)
