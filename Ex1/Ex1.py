with open('score.txt', 'r') as file:
    score = file.read().split("\n")

count = 0 

for i in score:
    if int(i) >= 50:
        count += 1 

print(count)