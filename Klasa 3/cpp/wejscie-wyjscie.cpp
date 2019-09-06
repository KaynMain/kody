/*
 * wejscie-wyjscie.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	const int rozmiar= 50;
    char imie[rozmiar];
    cout << "Jak się nazywasz? ";
    cin.getline(imie,rozmiar);
    cout << "Witaj! " << imie << endl;
    
	return 0;
}
