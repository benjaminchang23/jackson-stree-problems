#include <algorithm>
#include <iostream>
#include <vector>

struct container
{
    std::string a;
    int b;
    std::string c;
};

struct hash_fn
{
    std::size_t operator() (const container &con) const
    {
        std::size_t h1 = std::hash<std::string>()(con.a);
        std::size_t h2 = std::hash<int>()(con.b);
        std::size_t h3 = std::hash<std::string>()(con.c);

        return h1 ^ h2 ^ h3;
    }
};

inline std::ostream& operator << (std::ostream &o, const container &con)
{
    o << "a: " << con.a << " ";
    o << "b: " << con.b << " ";
    o << "c: " << con.c << " ";

    return o;
}

struct compare_struct
{
    bool a_first = true;

    bool operator() (const container &left, const container &right)
    {
        int comp = left.a.compare(right.a);
        std::cout << "compare: " << left << " - " << right << " - " << comp << std::endl;
        bool post = comp < 0 ? false : true;

        return post;
    }
};

int main()
{
    container con_0 {"1a0fe7e4-d1f2-4d34-a6aa-968f90180259", 1, "con_0"};
    container con_1 {"bf42f642-65e3-4dba-ab0c-c2a2a7eba44d", 8, "con_1"};
    container con_2 {"033567ce-14dd-462f-bdfb-c7ab05e01c7d", 3, "con_2"};
    container con_3 {"dd196de3-9c64-46bf-9046-585bf6667909", 1, "con_3"};

    std::vector<container> vec;

    vec.emplace_back(con_0);
    vec.emplace_back(con_1);
    vec.emplace_back(con_2);
    vec.emplace_back(con_3);

    compare_struct compare;
    compare.a_first = false;

    std::sort(vec.begin(), vec.end(), compare);

    for (const auto & con : vec)
    {
        std::cout << con << std::endl;
    }

    return 0;
}