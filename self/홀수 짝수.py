numbers = range(1, 11)

odd_numbers = []

for odd in numbers:
    if odd % 2 == 1:
        odd_numbers.append(odd)
        print(odd_numbers)

even_numbers = [even for even in numbers if even % 2 == 0]
print(even_numbers)
