import sys, traceback, Ice
import Demo

class PrinterI(Demo.Printer):                                     # Class Printer Interface
    def printString(self , s , current=None):                     # Method printString write  on StdOut the string.
        print s
    def printInteger(self , n , current=None):                    # Method printInteger write on StdOut the Integer.
        print n

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)                                                             # Inicialize with call Ice.initialize the object adapter

    adapter = ic.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000") # Object adapter Address and name "Object identity"

    object = PrinterI()                                                                       # We create a servant for our Printer interface by instantiating a PrinterI object.

    adapter.add(object, ic.stringToIdentity("SimplePrinter"))                                 # We activate the adapter by calling its activate method.
                                                                                              # The string "SimplePrinter" is the name of the Ice object, important inside client.

    adapter.activate()                                                                        # Call activate to servant wait request of client.

    ic.waitForShutdown()                                                                      # Call waitForShutdown suspends the calling thread until the server
                                                                                              # implementation terminates.


# Exception duo to ice communications and wrong dispathes and messages.
except:
    traceback.print_exc()
    status = 1

# It destroys the communicator (if one was created successfully) this is essential in order to correctly finalize.
if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)
