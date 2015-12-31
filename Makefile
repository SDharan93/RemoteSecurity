FLASK += python app/run.py &

all: run

build: remoteSecurity;

run: app/run.py;

clean: ; rm -f remoteSecurity.o remoteSecurity

install:
		sudo pip install twilio
