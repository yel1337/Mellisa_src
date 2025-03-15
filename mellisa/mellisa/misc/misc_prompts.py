import time
from datetime import datetime

class Misc:
    def misc_start(self):
        execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{execution_time}] Crawling...")
        time.sleep(2)

    def misc_output(self):
        print("")
        output_filePath = "/home/user/Mellisa/mellisa/mellisa/output/domain.json"
        print(f"Output file saved in: {output_filePath}")

    def misc_saving(self):
            execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{execution_time}] PARAMETERS FOUND")
            time.sleep(1)
            print(f"[{execution_time}] Scraping...")
            print(f"[{execution_time}] Saving...")
            time.sleep(2)