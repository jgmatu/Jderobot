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
    int status = 0;                       /* Value of status process for system */
    Ice::CommunicatorPtr ic;              /* Type of Object adapter and proxy Adapter */
    
    /* Code Server */ 
    try {
        ic = Ice::initialize(argc, argv);                                                     /* Initialize type ic pointer with the call Ice::initialize */
        Ice::ObjectAdapterPtr adapter =                                                       /* Object adapter Server Implementation */
            ic->createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000"); /* We create an object adapter by calling createObjectAdapterWithEndpoints on the Communicator instance. and default to protocol TCP/IP */
        Ice::ObjectPtr object = new PrinterI;                                                 /* Built-in Object Adapter */  
        adapter->add(object, ic->stringToIdentity("SimplePrinter"));
        adapter->activate();
        ic->waitForShutdown();
    
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
