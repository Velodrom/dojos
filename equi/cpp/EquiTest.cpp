#include <gtest/gtest.h>

int equi(int inputArr[], int arrayLen)
{
    // Find equilibrium index of inputArr
    int sum_left = 0;
	int sum_right = 0;

	for(int i = 0;i < arrayLen;i++)
	{
		for(int j = 0;j < arrayLen; j++)
		{
			if(j < i) sum_left += inputArr[j];
			if(j > i) sum_right += inputArr[j];
		}

		//Return the first equilibrium index found
		if(sum_right == sum_left) return i;

		//Reset the sum variables to continue iterating
		sum_left = 0;
		sum_right = 0;
	}

	//In case there is no equilibrium index
	return -1;
}

TEST(EquiTest, EmptyArrayReturnsZero)
{
    const int arrayLen = 0;
    int inputArr[arrayLen] = {};
    int equiIndex = equi(inputArr, arrayLen);
    int expectedEquiIndex = -1;
    ASSERT_EQ(expectedEquiIndex, equiIndex);
}

TEST(EquiTest, NonEmptyArray)
{  
    int A[] = {2,-3,4,-2,1};
    int equiIndex = equi(A, sizeof(A)/sizeof(int));
    int expectedEquiIndex = 0;
    ASSERT_EQ(expectedEquiIndex, equiIndex);
}
