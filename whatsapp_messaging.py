**from twilio.rest import Client


def msg_mom_and_dad(event=None, context=None):
    # get your sid and auth token from twilio
    twilio_sid = '***'
    auth_token = '---'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send them the message
    contact_directory = {'my_Tele2': '+79525805836'}

    for key, value in contact_directory.items():
        message = whatsapp_client.messages.create(
            body='good morning {} !'.format(key),
            from_='whatsapp:+14155238886',
            to='whatsapp:' + value,

        )

        print(message.sid)


if __name__ == '__main__':
    print('Run mode.')
    msg_mom_and_dad()

