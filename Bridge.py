# Implementor
class MessageSender:
    def send_message(self, subject, body):
        """___"""

# Concrete Implementors  
class EmailSender(MessageSender):
    def send_message(self, subject, body):
        print(f"Sending Email : {subject} --- {body}")
      
class SMSSender(MessageSender):
    def send_message(self, subject, body):
        print(f"Sending SMS : {subject} --- {body}")
        
# Abstraction
class Notification:
    def __init__(self, sender : MessageSender):
        self.sender = sender
        
    def notify(self, subject, body):
        self.sender.send_message(subject, body)
        

# Client Code
if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSSender()
    notif = Notification(email_sender)
    notif.notify("Invitation", "Come to my party tomorrow.")