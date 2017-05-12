#include <iostream>

class Solution
{
public:
	int rangeBitwiseAnd(int m, int n)
	{
		while (n>m) {
    	n = n & (n-1);
  	}
  	return n;
	}
};

/**
 * @brief    Problem 201 - Bitwise AND of Numbers Range | https://leetcode.com/problems/bitwise-and-of-numbers-range/#/description
 */
int main()
{
  int m = 5;
  int n = 7;
  Solution s;
  int val = s.rangeBitwiseAnd(m,n);
  std::cout << val << "\n";
  return 0;
}