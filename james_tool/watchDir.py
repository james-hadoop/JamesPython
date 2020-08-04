# -*- coding: utf-8 -*-

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


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

    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))
            if event.src_path.endswith(".txt"):
                time.sleep(1)


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    folder = "./"
    observer.schedule(event_handler, folder, False)
    print(f"当前监控的目录：{folder}")
    observer.start()
    observer.join()
