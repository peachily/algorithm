word = input().upper()

blank = [0] * 26

for alphabets in word:
    index = ord(alphabets) - 65
    blank[index] += 1

frequent = max(blank)

if blank.count(frequent) > 1:
    answer = "?"
else: answer = chr(blank.index(frequent) + 65)

print(answer)