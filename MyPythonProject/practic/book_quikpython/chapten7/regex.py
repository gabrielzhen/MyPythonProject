import re
phonenumber=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phonenumber.search('mynumber is 444-555-4445 and 444-555-4446')
print(mo)
print(type(mo))
