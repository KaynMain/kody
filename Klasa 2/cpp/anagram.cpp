/*
 * anagram.cpp
 * 
 * Ala ma kota, a kot ma Alę!
 * alA am atok, a tok am ęlA!
 */


#include <iostream>

using namespace std;

// anagram() - funkcja odwraca znaki w pojedyńczym wyrazie
// wyrazy() - funkcja dzieli tekst na wyrazy

int zlicz(char tb[]) {
    int i = 0;
    while(tb[i] != '\0') i++;
    return i;
}

void wyswietl(char tekst[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout << tekst[i];
    }
}

void anagram(char tb[], int roz) {
    for(int i = roz - 1; i >= 0; i--) {
        cout << tb[i];
    }
}

int main(int argc, char **argv)
{
	const int roz = 50;
    char tekst[roz]; 
    cout << "Podaj wyraz: ";
    cin.getline(tekst, roz);
    wyswietl(tekst, cin.gcount());
    cout << endl;
    anagram(tekst, cin.gcount());
    cout << endl;
	return 0;
}

