print("Enter a number between 0 and 1000:")

target = int(input())

answer = 0

if target > 1000:
    print("Too big, enter a number between 0 and 1000")
else:
    for even in range(2, target+1, 2):
        answer += even
print(answer)