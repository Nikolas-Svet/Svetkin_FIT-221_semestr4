//
// Create.cpp
//
#include <iostream>
#include <unknwn.h> // Объявление IUnknown
#include "create.h"

using namespace std;

typedef IUnknown* (*CREATEFUNCPTR)();

IUnknown* CallCreateInstance(char* name)
{
    // Загрузить в процесс динамическую библиотеку
    HINSTANCE hComponent = ::LoadLibrary(name);

    if (hComponent == NULL)
    {
        cout << "CallCreateInstance:\tError: Cannot load component."
        << endl;
        return NULL;
    }

    // Получить адрес функции CreateInstance
    CREATEFUNCPTR CreateInstance
    = (CREATEFUNCPTR)::GetProcAddress(hComponent, "CreateInstance");

    if (CreateInstance == NULL)
    {
        cout  << "CallCreateInstance:\tError: "
		      << "Cannot find CreateInstance function."
		      << endl ;
		return NULL ;
    }
    return CreateInstance();
}
