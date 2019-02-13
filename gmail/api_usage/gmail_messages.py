# Gmail Messages using API

def show_message_threads(service):
    threads = service.users().threads().list(userId='me').execute().get('threads', [])
    print('Here are Subject of your email messages:')

    for thread in threads:
        tdata = service.users().threads().get(userId='me', id=thread['id']).execute()
        nmsgs = len(tdata['messages'])

        if nmsgs > 1:  # skip if <1 msgs in thread
            msg = tdata['messages'][0]['payload']
            subject = ''
            for header in msg['headers']:
                if header['name'] == 'Subject':
                    subject = header['value']
                    break
            if subject:  # skip if no Subject line
                print('- %s (%d msgs)' % (subject, nmsgs))
