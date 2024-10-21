Initdata = []
Between_18_19 = []
with open('prifile.txt', 'r') as file:
    Data = file.read().splitlines()


for i in Data:
    Split = i.split()
    Initdata.append(Split) 

for i in Initdata:
    if int(i[2]) in range(18,20):
        Between_18_19.append(i)
    

for i in Between_18_19:
    print(i)