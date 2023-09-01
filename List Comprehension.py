s = "This is nice"
'''
li = []
for l in s:
    li.append(l)

print (li)
'''

li = [ l for l in s if l!=' ' and l!='i']
print (li)

#monoi
liOfNumbers = [x for x in range(10) if x%2 != 0]
print(liOfNumbers)
#zigoi
liOfNumbers = [x for x in range(10) if x%2 == 0]
print(liOfNumbers)