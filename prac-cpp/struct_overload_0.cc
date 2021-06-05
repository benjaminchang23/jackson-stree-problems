#include <iostream>

struct container
{
    int a;
};

inline std::ostream& operator << (std::ostream &o, const container &con)
{
    o << "a: " << con.a;
    return o;
}

int main()
{
    container con {4};

    std::cout << con << std::endl;

    return 0;
}