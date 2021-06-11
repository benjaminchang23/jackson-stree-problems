#include <iostream>
#include <unordered_map>

struct container
{
    int a;
    int b;
    std::string c;
};

struct hash_fn
{
    std::size_t operator() (const container &con) const
    {
        std::size_t h1 = std::hash<int>()(con.a);
        std::size_t h2 = std::hash<int>()(con.b);
        std::size_t h3 = std::hash<std::string>()(con.c);

        return h1 ^ h2 ^ h3;
    }
};

inline bool operator == (const container &left, const container &right)
{
    return left.a == right.a && left.b == right.b && left.c == right.c;
}

inline std::ostream& operator << (std::ostream &o, const container &con)
{
    o << "a: " << con.a << " ";
    o << "b: " << con.b << " ";
    o << "c: " << con.c << " ";
    return o;
}

int main()
{
    container con_0 {4, 5, "con_0"};
    container con_1 {6, 8, "con_1"};
    container con_2 {1, 3, "con_2"};

    container con_no_key {0, 0, "con_none"};
    container con_0_key {4, 5, "con_0"};
    container con_1_key {6, 8, "con_1"};
    container con_2_key {1, 3, "con_2"};

    std::unordered_map<container, std::string, hash_fn> map;

    map.emplace(con_0, "con0");
    map.emplace(con_1, "con1");
    map.emplace(con_2, "con2");

    auto it_0 = map.find(con_0_key);
    
    if (it_0 != map.end())
    {
        std::cout << it_0->second << " " <<  it_0->first << std::endl;
    }
    else
    {
        std::cout << "it_0 not found" << std::endl;
    }

    auto it_1 = map.find(con_1_key);
    
    if (it_1 != map.end())
    {
        std::cout << it_1->second << " " << it_1->first << std::endl;
    }
    else
    {
        std::cout << "it_1 not found" << std::endl;
    }

    auto it_2 = map.find(con_2_key);
    
    if (it_2 != map.end())
    {
        std::cout << it_2->second << " " << it_2->first << std::endl;
    }
    else
    {
        std::cout << "it_2 not found" << std::endl;
    }

    auto it_3 = map.find(con_no_key);
    
    if (it_3 != map.end())
    {
        std::cout << it_3->second << " " << it_3->first << std::endl;
    }
    else
    {
        std::cout << "it_3 not found" << std::endl;
    }


    return 0;
}