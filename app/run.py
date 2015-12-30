from flask import Flask, request, redirect
import twilio.twiml as twiml
import motion.common.var as var
from status import runningStat

app = Flask(__name__)
#used to keep track of state of the program
running = runningStat()

def runApp():
    if running.getRunning() == False:
        print "start Processes"
        running.setRunning(True)
        file = open("motion/common/.response.txt", "w")
        file.write("Zelda")
        file.close()
        return "started monitoring"

def stopApp():
    if running.getRunning() == True:
        print "stopping Processes"
        running.setRunning(False)
        file = open("motion/common/.response.txt", "w")
        file.write("Mario")
        file.close()
        return "stopped monitoring"

@app.route("/", methods=['GET', 'POST'])
def response():
    #get the body of text from sms message
    fromMessage = request.form['Body']
    toMessage = "please message using a proper command"

    if fromMessage == var.START:
        toMessage = runApp()

    elif fromMessage == var.STOP:
        toMessage = stopApp()

    #send the message
    response = twiml.Response()
    response.message(toMessage)
    return str(response)

if __name__ == "__main__":
    app.run(debug = True)
