CXX ?= g++

CXXFLAGS += -c -Wall $(shell pkg-config --cflags opencv)
LDFLAGS += $(shell pkg-config --libs --static opencv)

build: secuirtyCam;

secuirtyCam: securityCam.o;
	$(CXX) $< -o $@ $(LDFLAGS)

securityCam.o: securityCam.cpp;
	$(CXX) $< -o $@ $(CXXFLAGS)

clean: ; rm -f securityCam.o secuirtyCam
