//
// Create.cpp
//
#include <iostream>
#include <unknwn.h> // ���������� IUnknown
#include "create.h"

using namespace std;

typedef IUnknown* (*CREATEFUNCPTR)();

IUnknown* CallCreateInstance(char* name)
{
    // ��������� � ������� ������������ ����������
    HINSTANCE hComponent = ::LoadLibrary(name);

    if (hComponent == NULL)
    {
        cout << "CallCreateInstance:\tError: Cannot load component."
        << endl;
        return NULL;
    }

    // �������� ����� ������� CreateInstance
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
