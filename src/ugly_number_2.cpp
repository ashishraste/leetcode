#include <stdio.h>
#include <iostream>
#include <queue>
#include <math.h>

using namespace std;

/**
 * @brief     Class providing the heap-based solution for finding ugly numbers.
 */
class HeapSolution
{
public:
  /**
   * @brief     Finds the n-th ugly number.
   * 
   * @param n   n-th ugly number to find.
   * @return    n-th ugly number found among a list of generated ugly-numbers.
   */
  int nthUglyNumber(int n) {
    priority_queue<int, vector<int>, greater<int>> heap;
    heap.emplace(1);
    int ugly_num;
    for (int i=0; i<n; ++i) {
      ugly_num = heap.top();  // pick and pop a minimum value from the heap to generate further ugly-numbers.
      heap.pop();
      if (ugly_num % 2 == 0)
        heap.emplace(ugly_num * 2);
      else if (ugly_num % 3 == 0) {
        heap.emplace(ugly_num * 2);
        heap.emplace(ugly_num * 3);
      }
      else {
        heap.emplace(ugly_num * 2);
        heap.emplace(ugly_num * 3);
        heap.emplace(ugly_num * 5);
      }
    }
    return ugly_num;
  }
};

/**
 * @brief     Class providing the DP solution (bottom-up approach).
 * 
 * @param n   n-th ugly number to find.
 * @return    n-th ugly number found among a list of generated ugly-numbers.
 */
class DPSolution
{
public:
  int nthUglyNumber(int n) {
    vector<int> numbers;
    numbers.push_back(1);  // one of the base-numbers.
    int b1=2, b2=3, b3=5;  // base numbers, every number generated will be multiples of these numbers.
    int idx2=0, idx3=0, idx5=0;  // indexes for each of the base numbers, to remember the number with which they were previously multiplied.
    int min_num;
    // Note that a multiple of one base number could also be a multiple of the other base number.
    for (int i=1; i<n; ++i) {
      min_num = min(min(b1,b2),b3);
      numbers.push_back(min_num);
      if (min_num == b1) {  // generate a multiple of 2.
        b1 = 2 * numbers[++idx2];  
      }
      if (min_num == b2) {  // generate a multiple of 3. 
        b2 = 3 * numbers[++idx3];
      }
      if (min_num == b3) {  // generate a multiple of 5.
        b3 = 5 * numbers[++idx5];
      }
    }
    return numbers[n-1];
  }
};

/**
 * @brief     Problem 264 - Ugly Number II | https://leetcode.com/problems/ugly-number-ii/#/description
 */
int main(int argc, char** argv) 
{
  int num = 42;
  // HeapSolution *n = new HeapSolution();  
  // int u = n->nthUglyNumber(num);
  DPSolution *p = new DPSolution();
  int k = p->nthUglyNumber(num);  
  cout << k << "\n";
  delete(p);
  return 0;
}