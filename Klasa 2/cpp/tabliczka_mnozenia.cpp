/*
 * tabliczka_mnozenia.cpp
*/

#include <iostream>
#inlcude <iomanip>

using namespace std;

void tabliczka(int a, int b) {
    for (int i = 1; i <= a; i++) {
        for (int j = 1; j <= b; j++) {
            cout << setw(4) << i * j;
        }
        cout << endl; //znak nowej linii
    }
}

int main(int argc, char **argv)
{
	int a, b;   //deklaracja
    a = b = 0;  //inicjacja
    cout  << "Podaj zakres 1: ";
    cin  >> a;
    cout  << "Podaj zakres 2: ";
    cin  >> b;
    tabliczka(a, b);
	return 0;
}
