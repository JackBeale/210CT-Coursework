#include <iostream>
#include "iostream"
#include "string"

using namespace std;
int main(){
	string String1;
	cout << "Please enter the first word:";
	getline(cin, String1);

	string String2;
	cout << "Please enter the second word:";
	getline(cin, String2);

	string OutputString;
	int MinLength;
	int MaxLength;
	string Max;

	if (String1.length() > String2.length()){
		MinLength = String2.length();
		MaxLength = String1.length();
		Max = String1;
		}
	else{MinLength = String1.length();
		MaxLength = String2.length();
		Max = String2;
		}
	for (int i = 0; i < MinLength; ++i) {
		OutputString += String1.at(i);
		OutputString += String2.at(i);
		}
	if (String1.length() != String2.length()) {
		int x;
		x = MaxLength - MinLength;
		for (int j=0; j<=x; ++j) {
			OutputString += Max[MinLength+j];
			}
}
	cout << OutputString << "\n";
    return 0;
}
