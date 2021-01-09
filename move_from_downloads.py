import os,shutil,json,time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

USER_CONFIG_FILE="user.config"
f=open(USER_CONFIG_FILE,"r")
config=json.load(f)
USER=config["name"]

src_location="C:/Users/"+USER+"/Downloads"
dest_location="C:/Users/"+USER+"/Desktop/Downloaded Stuff"

class HandleDownloadFile(FileSystemEventHandler):

    def on_modified(self,event):
        size=-1
        copying=True
        while copying:
            s=os.path.getsize(src_location)
            if s==size:
                break
            else:
                size=os.path.getsize(src_location)
                time.sleep(10)
        print("Modifiy event recieved - "+event.src_path)
        for files in os.listdir(src_location):
            name,extension=os.path.splitext(files)
            if extension==".doc" or extension==".docx":
                destination=dest_location+"/docFolder"
                src=src_location+"/"+files
                shutil.move(src,destination)
                continue
            if extension==".exe":
                destination=dest_location+"/exeFolder"
                src=src_location+"/"+files
                shutil.move(src,destination)
                continue
            if extension==".htm" or extension==".html":
                destination=dest_location+"/htmlFolder"
                src=src_location+"/"+files
                shutil.move(src,destination)
                continue
            if extension==".pdf":
                destination=dest_location+"/pdfFolder"
                src=src_location+"/"+files
                shutil.move(src,destination)
                continue
            if extension==".png":
                destination=dest_location+"/pngFolder"
                src=src_location+"/"+files
                shutil.move(src,destination)
                continue
            if extension==".ppt" or extension==".pptx":
                destination=dest_location+"/pptFolder"
                src=src_location+"/"+files
                shutil.move(src,destination)
                continue
            if extension==".txt":
                destination=dest_location+"/txtFolder"
                src=src_location+"/"+files
                shutil.move(src,destination)
                continue
            if extension==".xls" or extension==".xlsx":
                destination=dest_location+"/xlsFolder"
                src=src_location+"/"+files
                shutil.move(src,destination)
                continue
            if extension=="":
                new_folder=files.split(".")[0]
                destination = dest_location+"/FolderFolder/"+new_folder
                if not os.path.exists(destination):
                    os.makedirs(destination)
                shutil.move(src_location+"/"+files,destination)
                continue
            if extension==".ini":
                continue
            destination=dest_location+"/otherFolder"
            src=src_location+"/"+files
            shutil.move(src,destination)

eventHandler=HandleDownloadFile()
observer=Observer()
observer.schedule(eventHandler,src_location,recursive=True)
observer.start()
print("Running")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
