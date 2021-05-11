# How do you find duplicate numbers in an array if it contains multiple duplicates?

s = [3, 3, 66, 66, 3, 4, 5, 5, 6, 66, 2, 1]
s_unique = list(set(s))
s_unique.sort()

seen = {}
s_duplicates = []
for x in s:
    if x not in seen: seen[x] = 1
    else:
        if seen[x] == 1: s_duplicates.append(x)
        seen[x] += 1
s_duplicates.sort()

print('Unique list: ', s_unique, '\nThe duplicates: ', s_duplicates)