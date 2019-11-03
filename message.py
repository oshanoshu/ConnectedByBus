from twilio.rest import Client

class Twilios:
    def __init__(self):
        self.account_sid = 'ACb8026c13c1410372f9bad5a8cc3f6985'
        self.auth_token = '4c5596db610934c4a7fe470aa0eb278d'
        

    def message(self,phoneNumber, details):
        client = Client(self.account_sid, self.auth_token)
        client.messages \
                    .create(
                        body=details,
                        from_='+12018905538',
                        to=phoneNumber
                    )
