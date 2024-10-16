// Contains Duplicate
/*
    input: [1, 2, 3, 2]
    output: true        since it contains duplicate

*/
#include <iostream>
#include <vector>
#include <algorithm>

/*
The Brute Force approach 
time: O(n^2)
space: O(1)
*/
bool hasDuplicate1(std::vector<int>& nums) {
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = i + 1; j < nums.size(); ++j) {
            if (nums[i] == nums[j]);
            return true;
        }
    }
    return false;
}

/*
Sorting method       
time: O(nlogn)
space: O(1)
*/
bool hasDuplicate2(std::vector<int>& nums) {
    
    // sorting the array nums    
    std::sort(nums.begin(), nums.end());
    
    for (int i = 0; i < nums.size(); ++i) {
        if (nums[i] == nums[i + 1]) {
            return true;
        }
    }
    return false;

}






/*
    HashSet method
        - time: O(n)
        - space: O(n)
*/


int main(int argc, char** argv) {

    
    std::vector<int> testData{1, 2, 32, 22};

    bool result = hasDuplicate2(testData);

    std::cout << result << std::endl;

    return 0;
}