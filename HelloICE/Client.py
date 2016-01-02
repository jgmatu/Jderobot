#!/usr/bin/python

import sys, traceback, Ice
import Demo

status = 0
ic = None

try:
    ic = Ice.initialize(sys.argv)                             # As for the server, we initialize the Ice run time by calling Ice.initialize.

    base = ic.stringToProxy("SimplePrinter:default -p 10000") # We create a proxy by calling stringToProxy on the communicator, with the string "SimplePrinter:default -p 10000"
                                                              # It contains a string with the object identity and the port number that were used by the server.

    printer = Demo.PrinterPrx.checkedCast(base)               # The proxy returned by stringToProxy is of type Ice.ObjectPrx
                                                              # But to actually talk to our printer, we need a proxy for a Demo::Printer interface, not an Object interface.
                                                              # A checked cast sends a message to the server, effectively asking "is this a proxy for a Demo::Printer interface?"
                                                              # If so, the call returns a proxy of type Demo.PrinterPrx; otherwise,
                                                              # if the proxy denotes an interface of some other type, the call returns None.

    if not printer:                                           # We test that the down-cast succeeded and, if not, throw an error message that terminates the client.
        raise RuntimeError("Invalid proxy")

    printer.printString("Hello World! with Ice :)!")          # We now have a live proxy in our address space and can call the printString method with arguments of method.

    
# Same as for the server: we use the same try and except blocks to deal with errors
except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()

    # Same as for the server: we use the same try and except blocks to deal with errors
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)
