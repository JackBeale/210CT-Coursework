// Binary search.cpp : Defines the entry point for the console application.

#include "iostream"
#include "math.h"
using namespace std;

int  Search(int Value, int TestH, int TestL)
{
	double Mid;
	Mid = floor((TestH + TestL) / 2);
	cout << Mid << endl;
	//Calculates the middle value.//
	if (Value == Mid) {
		cout << "FOUND!";
		return Value;
		//Outputs to the user when the PC has found the value being searched.//
	}
	else if (Value < Mid) {
		Search(Value, TestH, static_cast<int>(Mid));
	}
	else{
		Search(Value, static_cast<int>(Mid), TestL);
	}
	//The above else ifs, change the limits the PC has to search between.//
}

int main()
{
	cout << "Input the number you want to look for:" << endl;
	int Value;
	cin >> Value;
	Search(Value, 1, 2000);
	//Allows the user to input a number to search for, as well as set the boundaries.//
    return 0;
}
