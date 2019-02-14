# Gmail Messages using API

def show_message_content(service):
    threads = service.users().threads().list(userId='me').execute().get('threads', [])
    print('Here are Subject of your email messages:')

    for thread in threads:
        tdata = service.users().threads().get(userId='me', id=thread['id']).execute()
        nmsgs = len(tdata['messages'])

        if nmsgs > 1:  # skip if <1 msgs in thread
            msg = tdata['messages'][0]['payload']
            msg_from = ''
            unsubscribe_email = ''

            for header in msg['headers']:
                if header['name'] == 'From':
                    msg_from = header['value']
                if header['name'] == 'List-Unsubscribe':
                    unsubscribe_email = header['value']
                    break


            if msg_from:  # skip if no Subject line
                print('- MESSAGE SENDER: %s   UNSUBSCRIBE EMAIL: %s' % (msg_from, unsubscribe_email))