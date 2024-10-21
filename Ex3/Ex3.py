with open('datastory.txt', 'r') as file:
    InitData = file.read()

ValidValue = ['a','e','i','o','u']
Count = [['a',0],['e',0],['i',0],['o',0],['u',0]]

for i in InitData:
    if i in ValidValue:
        if i == 'a':
            Count[0][1] += 1
        elif i == 'e':
            Count[1][1] += 1
        elif i == 'i':
            Count[2][1] += 1
        elif i == 'o':
            Count[3][1] += 1
        elif i == 'u':
            Count[4][1] += 1

with open('result.txt', 'w') as file:
    ResultData = f'Story\nthe monkey runs in the jungle. the monkey is hungry.he spots a\nbanana in a tree. it is big and yellow. he climbs up the tree.\nhe eats the banana. he sees another banana. he eats that one too.\nthe monkey is hungry no more.\nCount Vowel (a,e,i,o,u)\nCount of character a = {Count[0][1]}\nCount of character e = {Count[1][1]}\nCount of character i = {Count[2][1]}\nCount of character o = {Count[3][1]}\nCount of character u = {Count[4][1]}'
    file.write(ResultData)