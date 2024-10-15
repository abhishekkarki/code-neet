// 118. Pascal's Triangle

#include <iostream>
#include <vector>

std::vector<std::vector<int>> generate(int numRows) {
    // creating a 2D vector to store the results
    std::vector<std::vector<int>> pascalTriangle(numRows);

    // Iterating the vector
    for (int i=0; i < numRows; ++i) {
        // Resizing the internal rows
        pascalTriangle[i].resize(i+1);

        // putting 1 at the first and the last position
        pascalTriangle[i][0] = pascalTriangle[i][i] = 1;

        // Filling the middle elements if exist
        for(int j=1; j<i; ++j) {
            pascalTriangle[i][j] = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j];
        }
    }
    return pascalTriangle;

}

int main() {
    std::vector<std::vector<int>> resultPascalTriangle = generate(5);

    for(int i=0; i<resultPascalTriangle.size(); ++i) {
        for(int j=0; j<resultPascalTriangle[i].size(); ++j) {
            std::cout << resultPascalTriangle[i][j] << " ";
        }
        std::cout << std::endl;
    }
}