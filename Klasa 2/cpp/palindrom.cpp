/*
 * palindrom.cpp
 */


#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(char tab[], int roz) {
    bool czyPal = true;
    for(int i = 0; i < roz / 2; i++) {
        if (tab[i] == tab[roz-1-i])
            ; // instrukcja pusta
        else {
            czyPal = false;
            break;
        }
    }
    return czyPal;
}

int main(int argc, char **argv)
{
	const int rozmiar = 20;
    char tekst[rozmiar];
    cout << "Podaj wyraz: ";
    cin.getline(tekst, rozmiar);
    if (palindrom(tekst, strlen(tekst))) 
        cout << "Palindrom";
    else {
        cout << "The thing";
    }
	return 0;
}
