#include <Ice/Ice.h>                          /* Include Ice in C++ program */
#include <Printer.h>                          /* Include our Slice module Generated */

using namespace std;
using namespace Demo;


int 
main(int argc, char* argv[])
{
	int status = 0;	                             /* Same that server status process to System */
	Ice::CommunicatorPtr ic;                     /* Same  type of variable to Client process */
	
	/* Code Client */
	try {
		ic = Ice::initialize(argc , argv);					    /* Same as Server */
		Ice::ObjectPrx base = ic->stringToProxy("SimplePrinter:default -p 10000");  /* Obtain a proxy for the remote printer. We create a proxy by calling stringToProxy on the communicator, with the string "SimplePrinter:default -p 10000". Note that the string contains the object identity and the port number that were used by the server. */
		PrinterPrx printer = PrinterPrx::checkedCast(base);
		if (!printer)
			throw "Invalid Proxy";
		printer->printString("Ice Hello world!! :)");
	
	/* Exceptions of Client first for Ice communications and later for messages errors */
	} catch (const Ice::Exception& ex){
		cerr << ex << endl;
		status = 1;
	} catch (const char* msg){
		cerr << msg << endl;
		status = 1;
	}
	/* If ic created Destroy it */
	if (ic)
		ic->destroy();
	return status;
}
