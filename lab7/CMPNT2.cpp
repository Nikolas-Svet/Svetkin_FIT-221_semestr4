//
// Cmpnt1.cpp
// To compile, use: cl /LD Cmpnt1.cpp GUIDs.cpp UUID.lib Cmpnt1.def
//
#include <iostream>
#include <objbase.h>
#include "trace.h"
using namespace std;
#include "Iface.h"

//void trace(const char* msg) { cout << "Component 1:\t" << msg << endl ;}

//
// Component
//
class CB : public IX, public IY
{
    // IUnknown implementation
    virtual HRESULT __stdcall QueryInterface(const IID& iid, void** ppv) ;
    virtual ULONG __stdcall AddRef() ;
    virtual ULONG __stdcall Release() ;

    // Interface IY implementation
    virtual void __stdcall Fy() { cout << "Fy" << endl ;}
    virtual void __stdcall Fx() { cout << "Fx" << endl ;}

public:
    // Constructor
    CB() : m_cRef(0) {}

    // Destructor
    ~CB() { trace("Destroy self.") ;}

private:
    long m_cRef ;
} ;

HRESULT __stdcall CB::QueryInterface(const IID& iid, void** ppv)
{
    if (iid == IID_IUnknown)
    {
        trace("Return pointer to IUnknown.") ;
        *ppv = static_cast<IY*>(this) ;
    }
    else if (iid == IID_IX)
    {
        trace("Return pointer to IX.") ;
        *ppv = static_cast<IX*>(this) ;
    }
    else if (iid == IID_IY)
    {
        trace("Return pointer to IY.") ;
        *ppv = static_cast<IY*>(this) ;
    }
    else
    {
        trace("Interface not supported.") ;
        *ppv = NULL ;
        return E_NOINTERFACE ;
    }
    reinterpret_cast<IUnknown*>(*ppv)->AddRef() ;
    return S_OK ;
}

ULONG __stdcall CB::AddRef()
{
    return InterlockedIncrement(&m_cRef) ;
}

ULONG __stdcall CB::Release()
{
    if (InterlockedDecrement(&m_cRef) == 0)
    {
        delete this ;
        return 0;
    }
    return m_cRef ;
}

//
// Creation function
//
extern "C" IUnknown* CreateInstance()
{
    IUnknown* pI = static_cast<IY*>(new CB) ;
    pI->AddRef() ;
    return pI ;
}
