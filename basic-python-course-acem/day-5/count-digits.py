a_long_number = 12345678900987654323456765432345676756436465897665364568754

a_long_number_str = str(a_long_number)

digit_count = dict()

# for digit in a_long_number_str:
#     digit_count[digit] = 0
    
for digit in a_long_number_str:
    if not digit_count.get(digit):
        digit_count[digit] = 0

    digit_count[digit] += 1

for digit, count in digit_count.items():
    print(f"{digit} is repeated {count} times.")