/*
 * znaki.cpp
 */


#include <iostream>

using namespace std;

void licz_znaki(char tab[]) {
    int i = 0;
    int biale = 0;
    int inter = 0;
    int licz = 0;
    while(tab[i] != '\0') {
        //~if (tab[i] == ' ' || tab[i] == '\t')
           //~biale++;
        //~else
            //~cout << tab[i];
        switch (tab[i]) {
            case ' ': biale++; break;
            case '\t': biale++; break;
            case ',': inter++; break;
            case '.': inter++; break;
            default: licz++; break;
        }
        i++; // zwiększenie indeksu
    }
    cout << "\nZnaków białych: " << biale << endl;
    cout << "\nInterpunkcyjnych: " << inter << endl;
    cout << "\nReszta: " << licz << endl;
}

void ascii(char tab[]) {
    int i = 0;
        while(tab[i] != '\0') {
            cout << (int)tab[i] << "";
            i++;
    }
}

void zamiana_liter(char tab[]) {
    int i = 0;
        while(tab[i] != '\0') {
            if (int)tab[i] < 97;
            int)tab[i]
            (char)(int)tab[i]
            i++;
    }
}

// A-Z ASCII 65-90, a-z ASCII 97-122
int main(int argc, char **argv)
{
    const int rozmiar = 20; // deklaracja stałej
	char znaki[20];  // deklaracja tablicy znakowej
    cout << "Jak się nazywasz? ";
    cin.getline(znaki, rozmiar);
    cout << "Cześć " << znaki << endl;
    // licz_znaki(znaki);
    ascii(znaki);
    zamiana_liter(znaki);
	return 0;
}
