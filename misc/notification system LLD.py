from collections import deque
from datetime import datetime

class User:
    def __init__(self, userId):
        self.id = userId
        self.preferences = {}
    
    def set_preferences(self, notification_type, channels):
        self.preferences[notification_type] = channels
    
    def get_preferences(self, notification_type):
        return self.preferences.get(notification_type, [])

class Notification:
    def __init__(self, notificationId, userId, type, content, timestamp):
        self.id = notificationId
        self.userId = userId
        self.type = type
        self.content = content
        self.timestamp = timestamp
        

class Channel:    
    def send(self, notification):
        raise NotImplementedError("This method should be implemented by subclasses")

class EmailChannel(Channel):
    def send(self, notification):
        print(f"Sending Email to user {notification.userId}: {notification.content}")

class SMSChannel(Channel):
    def send(self, notification):
        print(f"Sending SMS to user {notification.userId}: {notification.content}")

class PushChannel(Channel):
    def send(self, notification):
        print(f"Sending Push Notification to user {notification.userId}: {notification.content}")

class NotificationManager:
    def __init__(self):
        self.users = {}
        self.notificationQ = deque()
        self.channels = {
            "email": EmailChannel(),
            "sms": SMSChannel(),
            "push": PushChannel()
        }
    
    def add_user(self, userId):
        user = User(userId)
        self.users[userId] = user
        return user
    
    def create_notification(self, userId, notificationType, content):
        user = self.users.get(userId, None)
        if not user:
            raise Exception("User id invalid")
        
        notificationId = len(self.notificationQ) + 1
        notification = Notification(notificationId, userId, notificationType, content, datetime.now())
        self.notificationQ.append(notification)
        print(f"Notification {notificationId} added to queue for user {userId}")

    def dispatch_notifications(self):
        while self.notificationQ:
            notification = self.notificationQ.popleft()
            user = self.users.get(notification.userId, None)
            if not user:
                print(f"user {notification.userId} not found, skipping notification")
                continue

            preferredChannels = user.get_preferences(notification.type)
            if not preferredChannels:
                print(f"No preferred channels for {notification.type} notification for user {user.id}")
            for channelName in preferredChannels:
                channel = self.channels.get(channelName, None)
                if channel:
                    channel.send(notification)
                else:
                    print(f"Channel {channelName} unavailable")


system = NotificationManager()

user1 = system.add_user(1)
user2 = system.add_user(2)

user1.set_preferences("promo", ["email", "push"])
user2.set_preferences("alert", ["sms"])

system.create_notification(1, "promo", "90% off on next order")
system.create_notification(2, "alert", "Trial is expiring")

system.create_notification(2, "promo", "10 dollar off on indian food")

system.dispatch_notifications()

            

