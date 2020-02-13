#include <gtest/gtest.h>

int equi(int inputArr[], int arrayLen)
{
	// Find equilibrium index of inputArr
	
	//initialize LHS and RHS sums
	int sum_l = 0, sum_r = 0;
	
	//If the array length is zero
        if(arrayLen == 0){
                        return -1;
        }
	
	//Initialize RHS sum for index 0, with summation from index 1 to N-1
	for(int i=1; i<arrayLen; i++){
		 sum_r = sum_r + inputArr[i];
	}
	
	//move the index along the array and compare LHS and RHS sums
	for(int i=0; i<arrayLen; i++){
		if(sum_l == sum_r){
	        	return i;  //return the current index if equilibrium is satisfied
	        }
	       	
		//update LHS and RHS summatins for the next iteration
	        sum_l = sum_l + inputArr[i];
	        sum_r = sum_r - inputArr[i+1];
	 }
	         
	// Return -1 if no equilibrium index is found                       
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
