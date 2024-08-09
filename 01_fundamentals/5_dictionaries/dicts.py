
acronyms = {}

acronyms['LOL'] = 'Laught out Loud'

print(acronyms)

definition = acronyms.get('LOL')
print(definition)

if definition:
    print(definition)
else:
    print("Key doesn't exist")
