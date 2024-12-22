# testfile
from marrow.mailer import Mailer, Message

mailer = Mailer(dict(
        transport = dict(
                use = 'smtp',
                host = 'localhost', 
                port = 1025,
#                tls='starttls',
#                username='ruri9752@gmail.com',
#                password='Mikusu_Ruri1024'
)))
mailer.start()

message = Message(author="ruri9572@gmail.com", to="iferi0103@gmail.com")
message.subject = "Testing Marrow Mailer"
message.plain = "This is a test."
mailer.send(message)

mailer.stop()