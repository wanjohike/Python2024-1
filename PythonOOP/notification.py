import time
#  user the notification function from the plyer module
# round install to install it
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Ama Namna Gani My Friend!!",
            message = "Tume tenga shiling billion mia saba ya hawa kina mama mbona",
            timeout = 10
        )
        time.sleep(100)