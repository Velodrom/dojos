#include <gtest/gtest.h>
#include <string.h>

char FirstMissingAlphabet(std::string inputString)
{
    // Find first missing alphabet
    return 0;
}

TEST(FirstMissingAlphabet, OneCharacterInputMissingA)
{
    const std::string inputString = "b";
    const char expectedMissing = 'a';
    char foundMissing = FirstMissingAlphabet(inputString);
    ASSERT_EQ(expectedMissing, foundMissing);
}
