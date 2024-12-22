from marrow.mailer import Mailer, Message
from google.oauth2.credentials import Credentials

# 既存のトークンファイルから認証情報をロード
creds = Credentials.from_authorized_user_file('token.json', ['https://mail.google.com/'])

mailer = Mailer(dict(
    transport=dict(
        use='smtp',
        host='smtp.gmail.com',
        port=587,
        tls=dict(use=True),
        username='ruri9752@gmail.com',
        password=creds.token
    )
))
mailer.start()

message = Message(author="ruri9752@gmail.com", to="iferi0103@gmail.com")
message.subject = "Testing Marrow Mailer with OAuth"
message.plain = "This is a test using OAuth authentication."
mailer.send(message)

mailer.stop()
