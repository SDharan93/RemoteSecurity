import datetime
import dropbox
import os
from twilio.rest import TwilioRestClient

dropbox_access_token = os.environ['DROPBOX_ACCESS_TOKEN']
#print (dropbox_access_token)

timestamp = datetime.datetime.now().strftime("%h-%m-%S")
filename = "testing.avi"

f = open("testing.avi")
dropbox_client = dropbox.client.DropboxClient(dropbox_access_token)
response = dropbox_client.put_file(filename, f)
url = dropbox_client.media(response['path'])['url']
print (url)

client = TwilioRestClient()

message = client.messages.create(to = "+16473837027", from_= "+12898035077",
                                     body = "Alert: Movement has been detected!\nPlease check logs for the recording.",
                                     media_url = url)
