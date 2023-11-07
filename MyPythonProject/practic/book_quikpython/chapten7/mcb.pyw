#useage:python mcb.pyw save<keyword> save clipboard to keyword
#       python mcb.pyw <keyword> loads keyword to clipboard
#       python mcb.pyw list load all keywords to clipboard
import shelve,pyperclip,sys
mcbShelf=shelve.open('mcb')
#todo:save chlipboard content
if len(sys.argv)==3 and sys.argv[1].low()=='save':
    mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].low()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
#todu：list keywords and load content
mcbShelf.close()
