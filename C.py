import operator
f = input()

word = f
fin = ''
less = ''

seen = ''
charList = []

for c in word:
    if (c not in seen) and (word.count(c) > 1) and (word.count(c) % 2 == 0):
        charList.append({'char': c, 'count': int(word.count(c)/2)})
        word = word.replace(c, '')
        seen += c

if len(charList) > 0:
    charList.sort(key=operator.itemgetter('char'))
    
    for j in range(len(charList)):
        fin += charList[j]['char'] * charList[j]['count']
    
    less = 'Z'
    
    for c in word:
        if fin + c < less:
            less = fin + c + fin[::-1]
    
    print(less)
else:
    print(min(word))