/*
 * prostokat.cpp
 */

using namespace std;

int obwod(int a, int b)
{
    return 2 * a + 2 * b;
}

int pole(int a, int b)
{
    return a * b;
}

#include <iostream>

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    
    cout << "Podaj pierwszy bok: ";
    cin >> a;
    
    cout << "Podaj drugi bok: ";
    cin >> b;
    
    cout << a << " " << b << endl;
    
    cout << endl << "Obwód prostokąta: " << obwod(a, b) << endl;
    cout << "Pole prostokąta: " << pole(a, b) << endl;
    
	return 0;
}

