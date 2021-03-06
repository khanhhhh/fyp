import datetime
import os
from typing import List

log_folder = "./log"


class Log(object):
    folder: str

    def __init__(self):
        super(Log, self).__init__()
        if not os.path.isdir(log_folder):
            os.mkdir(log_folder)
        self.folder = os.path.join(log_folder, f"log_{datetime.datetime.now()}")
        os.mkdir(self.folder)

    def write(self, data: str, name: str = "default"):
        filepath = os.path.join(self.folder, f"{name}.log")
        if not os.path.isfile(filepath):
            with open(filepath, "w") as _:
                pass
        with open(filepath, "a") as fp:
            fp.write(f"{data}\n")
            print(f"{data}\n")

    def write_log(self, data: str, name: str = "default"):
        self.write(f"{datetime.datetime.now()}: {data}", name)

    def write_csv(self, data: List, name: str = "default"):
        self.write(",".join(map(lambda item: str(item), data)), name)


# default log
log = Log()
