#include <iostream>
#include <sstream>
#include <string>

int main()
{
	std::string str = "123456";
	// breaking words
	std::stringstream ss(str);

	// associating a string object with a stream
	size_t output = 3;

	// to read something from the stringstream object
	ss >> output;

	std::cout << output << std::endl;

	return 0;
}