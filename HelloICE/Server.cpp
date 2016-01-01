#include <Ice/Ice.h>    /* Include Ice library and modules to work with Ice... */
#include <Printer.h>    /* Include our Printer.h generate with Printer.ice Slide... */
 
using namespace std;
using namespace Demo;
 
/* Create object adapter in Server Code Virtual with skeleton of Printer.h  */
class PrinterI : public Printer {
public:
    virtual void printString(const string& s, const Ice::Current&);
};
 
/* We say the string get in Printer Interface goes to Standard Output */ 
void 
PrinterI::
printString(const string& s, const Ice::Current&)
{
    cout << s << endl;
}
 
int
main(int argc, char* argv[])
{
    int status = 0;                       /* Value of status process for operating system */
    Ice::CommunicatorPtr ic;              /* Type of Object adapter and proxy Adapter */
    
    /* Code Server */ 
    try {
        ic = Ice::initialize(argc, argv);                                                     /* Initialize type ic pointer with the call Ice::initialize */
        Ice::ObjectAdapterPtr adapter =                                                       /* Object adapter Server Implementation */
            ic->createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000"); /* We create an object adapter by calling createObjectAdapterWithEndpoints on the Communicator instance. and default to protocol TCP/IP */
        Ice::ObjectPtr object = new PrinterI;                                                 /* Built-in Object Adapter PrinterI object */  
        adapter->add(object, ic->stringToIdentity("SimplePrinter"));                          /* The string "SimplePrinter" is the name of the Ice object. */
        adapter->activate();                                                                  /* The server starts to process incoming requests from clients as soon as the adapter is activated. */
        ic->waitForShutdown();                                                                /*  call waitForShutdown. This call suspends the calling thread until the server implementation terminates, either by making a call to shut down the run time, or in response to a signal.  */
    
    /*  Exceptions first for Ice comunications later for msg  */  
    } catch (const Ice::Exception& e) {
        cerr << e << endl;
        status = 1;
    } catch (const char* msg) {
        cerr << msg << endl;
        status = 1;
    }
    /* ic Create correctly Object Adapter. */
    if (ic) {
        /* Clean ic Object Adapter. */
        try {
            ic->destroy();
        } catch (const Ice::Exception& e) {
            cerr << e << endl;
            status = 1;
        }
    }
    return status;
}
