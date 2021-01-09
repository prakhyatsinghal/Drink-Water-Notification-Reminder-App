import time
from plyer import notification
if __name__ == '__main__' :
 while True:
     notification.notify(
 			title = "**Please Drink Water Now!!",
 			message ="When you are tired and drink a lot of water, you will automatically feel more energized.",
 			app_icon = "C:\\Users\\MY HP\\Desktop\\Water Drinking Notifier\\glass-ico.ico",
 			timeout= 2
 	)
 		#	time.sleep(6)
 	 time.sleep(60*60)