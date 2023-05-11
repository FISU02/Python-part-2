tuple = (10,-3,4,9,12,-6,0)

max = tuple[0]
min = tuple [0]

for i in tuple:
    if min >i:
        min=i
    if max < i:
        max = i
print(f"Min : {min}\n Max = {max}")