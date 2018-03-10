def number_needed(a, b):
    pass
    total = 0
    hashTable = {'a': {}, 'b':{}}
    a_sorted = sorted(list(a))
    b_sorted = sorted(list(b))
    
    a_merged = ''.join(a_sorted)
    b_merged = ''.join(b_sorted)
    
    if a_merged == b_merged:
        return 0
    else:
        for letter in a_sorted:
            if hashTable['a'].get(letter):
                counter = hashTable['a'][letter]
                counter += 1
                hashTable['a'][letter] = counter
            else:
                hashTable['a'][letter] = 1
        
        for letter in b_sorted:
            if hashTable['b'].get(letter):
                counter = hashTable['b'][letter]
                counter += 1
                hashTable['b'][letter] = counter
            else:
                hashTable['b'][letter] = 1
    
    for letter in hashTable['a']:
        if letter in hashTable['b']:
            total += abs(hashTable['a'][letter] - hashTable['b'][letter])
        else:
            total += hashTable['a'][letter]
            
    for letter in hashTable['b']:
        if letter not in hashTable['a']:
            total += hashTable['b'][letter]

    return total

a = input().strip()
b = input().strip()

print(number_needed(a, b))
