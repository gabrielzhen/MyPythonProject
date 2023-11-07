import threading,time
def takesnap():
    time.sleep(5)
    print("Wake Up!")

threadObj=threading.Thread(target=takesnap)
threadObj.start()
print("program end")
