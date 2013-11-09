CC = /usr/bin/gcc
AR = ar
RANLIB = ranlib
SIZE = size

all: libpigpio.a tester

tester:		tester
	$(CC) -o tester pwmtest_withPIGPIO.c -L. -llibpigpio.a	

pigpio.o:
	$(CC) -o pigpio.o PIGPIO/pigpio.c 

LIB = libpigpio.a
OBJ = pigpio.o command.o

$(LIB):        $(OBJ)
	$(AR) rcs $(LIB) $(OBJ)
	$(RANLIB) $(LIB)
	$(SIZE) $(LIB)
