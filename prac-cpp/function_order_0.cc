#include <functional>
#include <iostream>
#include <vector>

struct pipeline_container
{
    int a = 0;
    int b = 0;
    int c = 0;
};

inline std::ostream& operator << (std::ostream &o, const pipeline_container &con)
{
    o << "a: " << con.a << ' ';
    o << "b: " << con.b << ' ';
    o << "c: " << con.c << ' ';

    return o;
}

using pipeline_callback = std::function<int(pipeline_container &con)>;

int OperationA(pipeline_container &container)
{
    std::cout << "Do operation a" << std::endl;
    container.a = container.a + 1;

    return 0;
}

int OperationB(pipeline_container &container)
{
    std::cout << "Do operation b" << std::endl;
    container.b = container.b + 1;

    return 0;
}

int OperationC(pipeline_container &container)
{
    std::cout << "Do operation c" << std::endl;
    container.c = container.c + 1;

    return 0;
}

int main()
{
    std::vector<pipeline_callback> functions;

    pipeline_container con;

    functions.emplace_back(OperationA);
    functions.emplace_back(OperationB);
    functions.emplace_back(OperationC);
    functions.emplace_back(OperationA);

    for (const auto & func : functions)
    {
        func(con);
        std::cout << con << std::endl;
    }

    return 0;
}