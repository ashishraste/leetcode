#include <iostream>

/**
 * @brief    Problem 201 - Bitwise AND of Numbers Range | https://leetcode.com/problems/bitwise-and-of-numbers-range/#/description
 */
int main()
{
  int m = 5;
  int n = 7;
  while (n>m) {
    n = n & (n-1);
  }
  std::cout << n << "\n";
  return n;
}