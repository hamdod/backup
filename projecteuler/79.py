with open('p079_keylog.txt') as file:
    attempts = file.read().splitlines()
file.close()

# delete duplicates
attempts = list(dict.fromkeys(attempts))
thisdic = {}
for attempt in attempts:
    for i in range(len(attempt)-1):
        for j in range(i+1,len(attempt)):
            if attempt[i] not in thisdic.keys():
                thisdic[attempt[i]]=[attempt[j]]
            else:
                if attempt[j] not in thisdic[attempt[i]]:
                    thisdic[attempt[i]].append(attempt[j])
print(thisdic)

keys_list = list(thisdic.keys())
str = ''
while len(keys_list)!=0:
    first = keys_list[0]
    for i in range(1,len(keys_list)):
        if len(thisdic[keys_list[i]])>len(thisdic[first]):
            print(thisdic[keys_list[i]],thisdic[first])
            first = keys_list[i]
    print(first, thisdic[first])
    str = str + first
    print(str)
    keys_list.remove(first)
