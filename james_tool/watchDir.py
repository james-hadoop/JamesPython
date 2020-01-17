# -*- coding: utf-8 -*-

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from txt2mail import txtMail


class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
            if event.src_path.endswith(".txt"):
                time.sleep(1)
                mail = txtMail()
                try:
                    mail.txt_send_mail(filename=event.src_path)
                except:
                    print("文本文件格式不正确")

    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))
            if event.src_path.endswith(".txt"):
                time.sleep(1)
                mail = txtMail()
                try:
                    mail.txt_send_mail(filename=event.src_path)
                except:
                    print("文本文件格式不正确")


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    dir = "./"
    observer.schedule(event_handler, dir, False)
    print(f"当前监控的目录：{dir}")
    observer.start()
    observer.join()
