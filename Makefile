CXX ?= g++

CXXFLAGS += -c -Wall -g -std=c++0x -pthread $(shell pkg-config --cflags opencv)
LDFLAGS += $(shell pkg-config --libs --static opencv)
PYLINK += -I/usr/include/python2.7
PYLIB += -lpython2.7

build: remoteSecurity;

remoteSecurity: remoteSecurity.o;
	$(CXX) $(PYLINK) $< -o $@ $(LDFLAGS) $(PYLIB)

remoteSecurity.o: remoteSecurity.cpp;
	$(CXX) $< -o $@ $(CXXFLAGS)

clean: ; rm -f remoteSecurity.o remoteSecurity

install:
		sudo pip install twilio
