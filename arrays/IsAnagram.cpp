/*
	Is Anagram
		- two strings, check if they both have same set of characters
		- like cat and tca
*/

#include <string>
#include <iostream>
#include <unordered_set>


bool isAnagram(std::string s, std::string t) {
	std::unordered_set<std::string> containsString1;

	// putting the string 1 in the containsString1
	for (auto character : s) {
		containsString1.insert(character);
	}

	for (auto characters : t) {
		if (containsString1.count(characters)) {
			continue;
		}
		else {
			return false;
		}

	}
	return true;
}


int main(int argc, char** argv) {
	std::string s{cat};
	std::string t{tac};

	std::cout << isAnagram(s, t) << std::endl;
}


