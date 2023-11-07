import pyperclip,sys,webbrowser
#todo get information from the paseboard
if len(sys.argv)>1:
    address=''.join(sys.argv[1:])
else:
    address=pyperclip.paste()
#todo open IE map
webbrowser.open('https://www.google.com/maps/place/'+address)
#todo past and search

