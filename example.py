from Kaprekar import split_sum, generate_kaprekar_list

print("9 is a Kaprekar Number: " + str(split_sum(9)))
print("45 is a Kaprekar Number: " + str(split_sum(45)))
print("777 is a Kaprekar Number: " + str(split_sum(777)))
print("9999 is a Kaprekar Number: " + str(split_sum(9999)))

print("Here is a small list of Kaprekar Numbers under 500: " + str(generate_kaprekar_list(500)))
