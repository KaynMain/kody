#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void generujliczby(int tab[], int ilosc){
    srand(time(NULL));
    for(int i = 0; i < ilosc; i++){
        tab[i] = rand() % 51;
    }
}

int main()
{
    int iloscliczb = 10;
    int tablica[iloscliczb + 1];
    int liczba;
    int i = 0;
    generujliczby(tablica, iloscliczb);
    cout << "Podaj liczbe z zakresu <0;50>" << endl;
    cin >> liczba;
    tablica[iloscliczb] = liczba;
    while(tablica[i] != liczba) i++;
    if(i < iloscliczb) cout << "Element znaleziony";
    else cout << "Element nieznaleziony";
    return 0; 
}
