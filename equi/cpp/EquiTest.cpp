#include <gtest/gtest.h>

int equi(int inputArr[], int arrayLen)
{
    // Find equilibrium index of inputArr
    return 0;
}

TEST(EquiTest, EmptyArrayReturnsZero)
{
    const int arrayLen = 0;
    int inputArr[arrayLen] = {};
    int equiIndex = equi(inputArr, arrayLen);
    int expectedEquiIndex = -1;
    ASSERT_EQ(expectedEquiIndex, equiIndex);
}
