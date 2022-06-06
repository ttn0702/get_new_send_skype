try:
    from skpy import Skype
    from os import walk
    from datetime import datetime
    from File_class import *
    from utils import *
    import time
except Exception as err1:
    print(err1) 

try:
    ID_GROUP = File_Interact('config.txt').read_file_line().split('=')[-1].strip()
    print(ID_GROUP)
    slogin = Skype('+84364680702','trungnghia11')
    channel = slogin.chats.chat(ID_GROUP)
    # contract = slogin.contacts
    # group1 = slogin.chats.recent()
    list_time = ['7:30','11:30','19:00']
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if now in list_time:
            run()

            mypath = './image'
            list_img = []
            for (dirpath, dirnames, filenames) in walk(mypath):
                list_img.extend(filenames)
                break


            for img in list_img:
                filePath = f'./image/{img}'
                name = img
                try:
                    channel.sendFile(open(filePath, "rb"), name, image=True)
                except:
                    pass

            print(now)
            time.sleep(120)
except Exception as err:
    print(err)
input()