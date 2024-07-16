import random as rd 
 
member = [ 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
] 
 
number = [] 
for num in range (0, len(member)): number.append(num) 
 
total = int(input(" Group  : ")) 
kel = [] 
for x in range(total): 
    sub= [] 
    kel.append(sub) 
 
count = 0 
while len(number) > 0: 
 
    random = rd.randint(0, len(number)-1) 
    result = number[random] 
    del (number[random]) 
 
    kel[count].append(member[result]) 
    if count == len(kel)-1:  
        count = 0 
    else:  
        count+=1 
nm = total-1 
for kel_sub in kel: 
    print("\n") 
    print(f".:Group {total-nm}:.") 
    for name in kel_sub: 
        print(f"{name}") 
    nm = nm - 1