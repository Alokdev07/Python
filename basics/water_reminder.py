import time
from plyer import notification

while True:
    notification.notify(
        title="💧 Drink Water Reminder",
        message="Baby, it's time to drink some water and stay hydrated ❤️",
        timeout=10  # Notification stays for 10 sec
    )
    # Wait for 2 hours (2 * 60 * 60 seconds)
    time.sleep(2 * 60 * 60)
