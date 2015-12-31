from flask import Flask, request, redirect
import os
import twilio.twiml as twiml
import motion.common.var as var
from status import runningStat
from subprocess import call, Popen, PIPE

app = Flask(__name__)
#used to keep track of state of the program
running = runningStat()

#starts the detection program
def runApp():
    #will only start program once
    if running.getRunning() == False:
        running.setRunning(True)
        #checks if the detection program exists
        if os.path.exists('launcher.py'):
            global process
            #launches the process for motion detection
            process = Popen(['python', 'launcher.py'], stdin=PIPE, stdout=PIPE)
            #flushes stdin for process so unneccessary data is not read
            process.stdin.flush()
            #sent for handshake
            process.stdin.write('Zelda\n')
        return "started monitoring"

#function stops the detection program
def stopApp():
    #if the program is already running
    if running.getRunning() == True:
        running.setRunning(False)
        global process
        process.stdin.flush()
        #Closes the motion detection program
        print process.communicate("Mario\n")[0]
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
    #used to track the detection process
    global process
    app.run(debug = True)
