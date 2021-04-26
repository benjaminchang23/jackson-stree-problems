#include <iostream>
#include <vector>

template <typename T>
void PrintVector(const std::vector<T> vec)
{
    for (auto element : vec)
    {
        std::cout << element << " ";
    }

    std::cout << std::endl;
}

class Base
{
public:
    Base(const std::vector<int> &vec)
    {
        vec_ = vec;
    }

    Base(Base const &rhs)
    {
        vec_ = rhs.vec_;
    }

    void operator = (const Base &base)
    {
        vec_ = base.vec_;
    }

    // move semantics means you can't use const, which will force a copy
    Base(Base &&rhs)
    {
        *this = std::move(rhs);
    }

    void PrintContents()
    {
        PrintVector<int>(vec_);
    }

    std::vector<int> vec_;
};

class Derived : Base
{
    Derived(Derived const &rhs) :
        Base(rhs)
    {
        std::cout << "Derived copy constructor" << std::endl;
    }

    Derived(Derived &&rhs) :
        Base(std::move(rhs)) // calls Base(Base&& rhs)
    {
        std::cout << "Derived move constructor" << std::endl;
    }

    std::vector<int> vec_;
};

int main()
{
    auto vec = std::vector<int>({1, 2, 3, 5, 4});

    Base base = Base(vec);

    return 0;
}