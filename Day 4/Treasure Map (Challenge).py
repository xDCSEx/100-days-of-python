line1 = ["0","0","0"]
line2 = ["0","0","0"]
line3 = ["0","0","0"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

print("Type your co-ordinates below")
position = input()

letter = position[0].lower()

abc = ["a","b","c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

# "The .index() method in Python returns the index (the position) of the first occurrence of a specified value within a list.
# It does not return the value itself."

print(f"{line1}\n{line2}\n{line3}")

print(letter_index)