import time
from plyer import notification
if __name__=="__main__":
 while True:
    notification.notify(
        title="Please Drink Water",
        message="Seems You Have Not Drunk Water in a While!",
        timeout=10 
        )
    time.sleep(60*60)