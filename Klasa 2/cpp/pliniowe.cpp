/*
 * pliniowe.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int n = 6;
    int szuk = 8;
    int tab[n+1] = {1, 5, 3, 8, 0, 6};
    int tab[n] = szuk; //wartownik
    int i = 0;
    while (tab[i] != szuk) i++;
    if (i < n)
        cout << "Znaleziony";
    else
        cout << "Nie znaleziony";
	return 0;
}

