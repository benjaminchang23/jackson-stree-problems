#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>

#include <openssl/md5.h>

// taken from https://stackoverflow.com/questions/1220046/how-to-get-the-md5-hash-of-a-file-in-c
// taken from https://insanecoding.blogspot.com/2011/11/how-to-read-in-file-in-c.html
const std::string MD5FromFile(const std::string& path)
{
    std::string contents;
    std::ostringstream oss;
    unsigned char result[MD5_DIGEST_LENGTH];

    std::ifstream input(path, std::ios::in | std::ios::binary);
    if (input)
    {
        input.seekg(0, std::ios::end);
        contents.resize(input.tellg());
        input.seekg(0, std::ios::beg);
        input.read(&contents[0], contents.size());
        input.close();
    }

    MD5((unsigned char*)contents.c_str(), contents.size(), result);

    oss << std::hex << std::setfill('0');
    for (auto c : result) oss << std::setw(2) << (int)c;

    return oss.str();
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    { 
        std::cout << "Must specify the file" << std::endl;
        exit(-1);
    }

    std::cout << "Using file: " << argv[1] << std::endl;

    std::cout << "MD5: " << MD5FromFile(argv[1]) << std::endl;

    return 0;
}
