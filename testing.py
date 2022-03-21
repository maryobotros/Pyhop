# from pycreate2 import Create2
# import time
#
# port = "/dev/tty.usbserial-DN025ZAZ"  # The port to connect to the Create2
# bot = Create2(port)
# bot.start()  # Start the Create2
# bot.safe()  # Put the Create2 into 'safe' mode so we can drive it, still provides protection
#
# sensors = bot.get_sensors()
# lb_left = sensors[36]
# lb_center_left = sensors[38]
# lb_front_left = sensors[37]
# lb_right = sensors[41]
# lb_center_right = sensors[39]
# lb_front_right = sensors[40]
#
# bot.drive_direct(100, 100)
# time.sleep(1)

dist = {'oxy': {'home': 20}, 'home': {'oxy': 20}}
print(dist['oxy'])