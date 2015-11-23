from twilio.rest import TwilioRestClient

client = TwilioRestClient()

message = client.messages.create(to = "+16473837027", from_= "+12898035077",
                                     body = "Alert: Movement has been detected!\nPlease check logs for the recording.")
