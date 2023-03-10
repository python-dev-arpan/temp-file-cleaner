import os
import send2trash
import shutil

userlogin = os.getlogin()

dir = "C:/Windows/Temp"
dir2 = f"C:/Users/{userlogin}/AppData/Local/Temp"


def delete_files(dir):
    os.chdir(dir)

    contents = os.listdir()

    if len(contents) > 0:
        for item in contents:
            try:
                send2trash.send2trash(item)
            except Exception as e:
                print(e)

shutil.copy("start.bat", fr"C:\Users\{userlogin}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start.bat")

delete_files(dir)
delete_files(dir2)
