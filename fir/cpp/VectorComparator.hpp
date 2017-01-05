#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

template<class Type>
bool ValuesEqual(Type valueA, Type valueB)
{
    bool valuesMatch = false;
    if (valueA == valueB)
        valuesMatch = true;

    return valuesMatch;
}

template<>
bool ValuesEqual<float>(float valueA, float valueB)
{
    bool valuesMatch = false;
    float relativeTolerance = 0.001;
    float absoluteTolerance = 0.00001;

    if (fabs(valueA-valueB) < absoluteTolerance)
    {
        valuesMatch = true;
    }
    else
    {
        // Always divide by the larger number to avoid div by zero
        float relativeError;
        if (fabs(valueA) > fabs(valueB))
            relativeError = fabs(valueA-valueB)/valueA;
        else
            relativeError = fabs(valueA-valueB)/valueB;

        if (relativeError < relativeTolerance)
            valuesMatch = true;
    }

    return valuesMatch;
}

template<class Type>
bool CompareVectors(vector<Type> vectorA, vector<Type> vectorB)
{
    bool vectorsMatch = true;
    int lengthA = vectorA.size();
    int lengthB = vectorB.size();

    if (lengthA == lengthB)
    {
        for (int idx = 0; idx < lengthA; idx++)
        {
            if (!ValuesEqual(vectorA[idx], vectorB[idx]))
            {
                printf("Vector mismatch at [%d]\nReceived: %10f\nExpected: %10f\n",
                       idx, vectorB[idx], vectorA[idx]);
                vectorsMatch = false;
                break;
            }
        }
    }
    else
    {
        printf("Vector length mismatch\nReceived: %d\nExpected: %d\n",
               lengthB, lengthA);
        vectorsMatch = false;
    }
    return vectorsMatch;
}