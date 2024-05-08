#include <iostream>
#include <objbase.h>
#include "trace.h"
#include "Iface.h"
#include "Create.h"

using namespace std;


// Client1
int main() {
    HRESULT hr;

    // Get the name of the component to use.
    char name[40];
    cout << "Enter the filename of a component to use [Cmpnt?.dll]: ";
    cin >> name;
    cout << endl;

    // Create component by calling the CreateInstance function in the DLL.
    trace("Get an IUnknown pointer.");
    IUnknown *pIUnknown = CallCreateInstance(name);
    if (pIUnknown == NULL) {
        trace("CallCreateInstance Failed.");
        return 1;
    }

    trace("Get interface IX.");

    IX * pIX;
    hr = pIUnknown->QueryInterface(IID_IX, (void **) &pIX);

    if (SUCCEEDED(hr)) {
        trace("Succeeded getting IX.");
        pIX->Fx();          // Use interface IX.
        pIX->Release();
    } else {
        trace("Could not get interface IX.");
    }

    IY * pIY;
    hr = pIUnknown->QueryInterface(IID_IY, (void **) &pIY);

    if (SUCCEEDED(hr)) {
        trace("Succeeded getting IY.");
        pIY->Fy();          // Use interface IX.
        pIY->Release();
    } else {
        trace("Could not get interface IY.");
    }

    IZ * pIZ;
    hr = pIUnknown->QueryInterface(IID_IZ, (void **) &pIZ);

    if (SUCCEEDED(hr)) {
        trace("Succeeded getting IZ.");
        pIZ->Fz();          // Use interface IX.
        pIZ->Release();
    } else {
        trace("Could not get interface IZ.");
    }

    trace("Release IUnknown interface.");
    pIUnknown->Release();

    return 0;
}


