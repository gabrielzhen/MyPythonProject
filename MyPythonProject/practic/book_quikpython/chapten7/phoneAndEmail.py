#finds phone adn email on the clipboard
#1 create phone relex
import re,pyperclip
phonerelex=re.compile(
r'''(
(\d{3}|\(\d{3}\))?
(\s|-|.)?
(\d{3})
(\s|-|.)
(\d{4})
)''',re.verbose
)
#2 create email relex
mailrelex=re.compile(
r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9]+
(\.[a-zA-Z]{2-4})
    )''',re.verbose
)
#3 find matches on the clipboard
text=str(pyperclip.paste())
matches=[]
for groups in phonerelex.findall(text):
    phonenum='-',join([groups[1],groups[3],groups[5]])
    matches.append(phonenum)

for groups in mailrelex.findall(text):
    matches.append(groups[0])

# copy to the clipboard
pyerclip.copy('\n'.join(matches))
print('\n'.join(matches))