#include <iostream>
#include <stdint.h>
#include <bitset>

using namespace std;

class Solution
{
public:
	uint32_t reverseBits(uint32_t n)
	{
		uint32_t tgt = 0x00000000;
		uint32_t mask = 0x00000001;
		for (int i=1; i<=32; ++i) {
			if (n & (mask << (i-1))) {
				tgt = tgt | (mask << (32-i));
				// cout << "tgt " << std::bitset<32>(tgt) << "\n";
			}
		}
		return tgt;
	}
};

/**
* @brief    Solution to Leetcode problem 190.
* @details  URL : https://leetcode.com/problems/reverse-bits/#/description
*/

int main()
{
	Solution s;
	uint32_t input = 43261596;
	cout << "input " << std::bitset<32>(input) << "\n";
	uint32_t r = s.reverseBits(input);
	cout << "output " << std::bitset<32>(r) << "\n";
	return 0;
}