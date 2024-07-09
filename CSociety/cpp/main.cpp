#include <iostream>  // Include the iostream library for input and output
#include <format>

int main() {  // Define the main function, the entry point of the program
    std::cout << "Hello, World!" << std::endl;  // Print "Hello, World!" to the console
    std::int x = 10;
    std::int y = 1;
    std::cout << x+y << std::endl;

    for (int i=0; i<10; i++){
     std::string output = std::format("I am in the {} loop", i+1);
     std::cout << output << std::endl;
    }
    return 0;  // Return 0 to indicate the program ended successfully
}
