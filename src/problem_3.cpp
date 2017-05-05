#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <map>

using namespace std;

class LongestSubstring 
{
public:
	int lengthOfLongestSubstring(const string& str) {
		map<char,int> mc;  // map of characters traversed
		size_t high = 0;
		size_t start = 0;
		for (int i=0; i < str.size(); ++i) {
			auto it = mc.find(str[i]);
			if (it == mc.cend()) {  // new character 
				mc.emplace(str[i],i);
			}
			else {  // character already present, update the biggest_idx if required
				if (it->second >= start) {   // update biggest_idx
					high = max(high,i-start);
					start = it->second + 1;
				}
				it->second = i; 
			}
		}
		high = max(high, str.size()-start);
		return high;
	}
};

int main(int argc, char** argv)
{
	LongestSubstring* pls = new LongestSubstring();
	// test
	cout << pls->lengthOfLongestSubstring(string("aab")) << "\n";
	return 0;
}