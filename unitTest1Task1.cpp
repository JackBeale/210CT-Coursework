#include "stdafx.h"
#include "CppUnitTest.h"
#include "../week1 Part1/CombineString.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{		
	TEST_CLASS(UnitTest1)
	{
	public:
		
		TEST_METHOD(TestMethod1)
		{
			// TODO: Your test code here
			Assert::AreEqual(combineStrings("d", "d"), string("dd"));
			Assert::AreEqual(combineStrings("d", ""), string("d"));
		}

	};
}