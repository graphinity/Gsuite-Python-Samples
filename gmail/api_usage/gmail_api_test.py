# Test Gmail API methods

from gmail.api_usage.gmail_credentials import credentials
from gmail.api_usage.gmail_messages_subject import show_message_threads
from gmail.api_usage.gmail_messages_content import show_message_content
from gmail.api_usage.gmail_labels import show_labels_threads

if __name__ == '__main__':
    service = credentials()
    # show_labels_threads(service=service)
    # show_message_threads(service=service)
    show_message_content(service=service)

