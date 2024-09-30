number = int(input("Enter a number: "))
number_str = str(number)

digits_list = [int(digit) for digit in number_str]
same = True

for i in range(0, len(digits_list)):
    if digits_list[i] != digits_list[len(digits_list) - i - 1]:
        same = False

if same:
    print("Palindrome")
else:
    print("Not Palindrome")

