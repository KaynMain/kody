/*
 * potega.cpp
 */


#include <iostream>

using namespace std;
// x0 =1 dla x <> 0
// xn = x(n-1)*x dla n = N+

float potega_re(float x, int n) {
    if (n == 0) return 1;
    return potega_re(x, n-1) * x;
}
    
int main(int argc, char **argv)
{   
	float podstawa;
    int wykladnik;
    cout << "Podstawa: "; cin >> podstawa;
    cout << "Wykladnik: "; cin >> wykladnik;
    cout << "Wynik: " <<potega_re(podstawa, wykladnik);
	return 0;
}

