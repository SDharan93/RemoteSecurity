CXX ?= g++

CXXFLAGS += -c -Wall $(shell pkg-config --cflags opencv)
LDFLAGS += $(shell pkg-config --libs --static opencv)

build: remoteSecurity;

remoteSecurity: remoteSecurity.o;
	$(CXX) $< -o $@ $(LDFLAGS)

remoteSecurity.o: remoteSecurity.cpp;
	$(CXX) $< -o $@ $(CXXFLAGS)

clean: ; rm -f remoteSecurity.o remoteSecurity

install:
		sudo pip install twilio
