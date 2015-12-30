FLASK += python app/runServer.py &
DETECT += python app/runApp.py &

all: run

build: remoteSecurity;

run: app/runApp.py app/runServer.py;

clean: ; rm -f remoteSecurity.o remoteSecurity

install:
		sudo pip install twilio
