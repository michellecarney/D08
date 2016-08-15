d = {'Daniel': 'blue', 'Someone': 'blue', 'Sometwo': 'red'}

def reverse_lookup(dict_, value):
    key_or_keys = []
    for k, v in dict_.items():
        if v == value:
            return k

print(reverse_lookup(d, "blue"))
print(reverse_lookup(d, "red"))