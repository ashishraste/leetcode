#include <iostream>
#include <unordered_map>
#include <vector>
#include <ostream>

// using namespace std; 

using ::std::string;
using ::std::vector;
using ::std::unordered_map;
using ::std::cout;

class Solution
{
public:
  int minMutation(string start, string end, vector<string>& bank) {
    unordered_map<string,char> geneDB;
    unordered_map<int,char> flipsDB;
    // For a database of the gene-bank.
    for (const string& s : bank) geneDB.emplace(s,1);

    // Find the indices of characters which are different, among source and target strings.
    // Store them in flipsDB.
    for (int i=0; i<8; ++i) {
      if (start[i] != end[i])       // character is different
      {
        flipsDB.emplace(i,end[i]);   // store the index and the target character
      }
    }
    cout << flipsDB.size() << "\n";
    bool notFound = false;

    // For every character-flip, form a new string and check whether it's in geneDB.
    for (const auto& it : flipsDB) {
      int idx = it.first;
      char ch = it.second;
      start[idx] = ch;
      auto search = geneDB.find(start);
      if (search != geneDB.end()) continue;
      else {
        notFound = true;
        break;
      }
    }
    if (!notFound) return flipsDB.size();
    else return -1;
  }
};


int main()
{
  // using ::std::string;
  // using ::std::cout;
  string start = "AACCGGTT";
  string end = "AAACGGTA";
  vector<string> bank = {"AACCGATT","AACCGATA","AAACGATA","AAACGGTA"};
  // bank.push_back(string("AACCGATT","AACCGATA","AAACGATA","AAACGGTA"));
  // bank.push_back(string("AACBPCDD"));
  // bank.push_back(string("AACBPCFD"));
  // bank.push_back(string("AACBPCFF"));

  Solution s;
  int num = s.minMutation(start,end,bank);
  // cout << num << "\n";

  return 0;
}