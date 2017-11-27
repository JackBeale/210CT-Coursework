#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
	string InputNumber;

	cout << "Please input 3 numbers";
	cin >> InputNumber;
	char Number1 = InputNumber.at(0);
	char Number2 = InputNumber.at(1);
	char Number3 = InputNumber.at(2);

	char x = Number1;
	int ix = (int)x - 48;

	char y = Number2;
	int iy = (int)y - 48;

	char z = Number3;
	int iz = (int)z - 48;

	int newInt = stoi(InputNumber);

	int sum = (ix*ix*ix) + (iy*iy*iy) + (iz*iz*iz);

	if (newInt == sum) {
		cout << "This is an =Armstrong number!";
	}
	else {
		cout << "This is not an Armstrong number";
	}
    return 0;
}
