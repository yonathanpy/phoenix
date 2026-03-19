import datetime

class Logger:
    def log(self, level, message):
        entry = f"[{datetime.datetime.now()}] [{level}] {message}"
        print(entry)
        with open("phoenix.log", "a") as f:
            f.write(entry + "\n")

logger = Logger()
