data = input()
dict = {'c=':1, 'c-':1, 'dz=':1, 'd-':1, 'lj':1, 'nj':1, 's=':1, 'z=':1}
for i in list(dict.keys()):
    data = data.replace(i, '_')

print(len(data))