import schedule
import time


schedule.every().day.at("19:00").do()


while True:
    schedule.run_pending()
    time.sleep(1)
