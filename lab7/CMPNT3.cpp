//#include <iostream>
//#include <objbase.h>
//#include "trace.h"
//#include "Iface.h"
//
////__declspec(dllexport) void trace(const char* msg) { std::cout << "Component 3:\t" << msg << std::endl; }
//
//class CC : public IX {
//public:
//    long m_cRef;
//
//    CC() : m_cRef(0) { trace("CC Constructor called."); }
//    virtual ~CC() { trace("CC Destructor called."); }
//
//    virtual HRESULT __stdcall QueryInterface(const IID& iid, void** ppv);
//    virtual ULONG __stdcall AddRef();
//    virtual ULONG __stdcall Release();
//
//    virtual void __stdcall Fx() { std::cout << "Fx from Component 3" << std::endl; }
//};
//
//HRESULT __stdcall CC::QueryInterface(const IID& iid, void** ppv) {
//    if (iid == IID_IUnknown) {
//        *ppv = static_cast<IX*>(this);
//    } else if (iid == IID_IX) {
//        *ppv = static_cast<IX*>(this);
//    } else {
//        *ppv = NULL;
//        return E_NOINTERFACE;
//    }
//    reinterpret_cast<IUnknown*>(*ppv)->AddRef();
//    return S_OK;
//}
//
//ULONG __stdcall CC::AddRef() {
//    return InterlockedIncrement(&m_cRef);
//}
//
//ULONG __stdcall CC::Release() {
//    if (InterlockedDecrement(&m_cRef) == 0) {
//        delete this;
//        return 0;
//    }
//    return m_cRef;
//}
//
//extern "C" __declspec(dllexport) IUnknown* CreateInstance() {
//    return static_cast<IX*>(new CC());
//}