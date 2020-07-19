

try:
    dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
    for x in dict_.keys():
        x + 'abc'
except TypeError:
    dict_.pop(12)
    dict_['12'] = 'age'
print(dict_)
