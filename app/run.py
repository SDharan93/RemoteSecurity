from flask import Flask, request, redirect
import twilio.twiml as twiml
from motion import

app = Flask(__name__)

@app.route("/", method=['GET', 'POST'])

def response():
    fromMessage = request.form['Body']
    toMessage = 'Hey %s, how are you today?' % (message)
    print toMessage

    response = twiml.Response()
    response.message(toMessage)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
