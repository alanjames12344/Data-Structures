import array

dic = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z'] }
res = set()

inp = int(input())
arr = array.array('i')
inp_len = 0
while inp > 1:
    temp = int(inp % 10)
    arr.append(temp)
    inp= inp/10
    inp_len += 1

for i in range(0,inp_len-1):
    x = int(arr[i])
    y = int(arr[i+1])
    if(y == 7 or y == 9):
        y = y%4
    else:
        y=y%3

    res.add(dic[x][0])
    res.add(dic[x][y])
temp = arr[inp_len-1]
res.add(dic[temp][0])
    
print(res)
print(len(res))