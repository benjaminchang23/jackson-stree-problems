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

// This is likely to get the compiler to do return value optimization and construct Base at the return value
Base Foo()
{
    Base base(std::vector<int>({2, 4, 6, 8}));
    base.PrintContents();
    return base;
}

Base FooButWorse()
{
    Base base(std::vector<int>({2, 4, 6, 8}));
    base.PrintContents();
    return std::move(base);
}

int main()
{
    auto vec = std::vector<int>({1, 2, 3, 5, 4});

    Base base_0 = Base(vec);
    Base base_1 = Foo();
    Base base_2 = FooButWorse();

    std::cout << "After construction, copy or in place" << std::endl;

    base_0.PrintContents();
    base_1.PrintContents();
    base_2.PrintContents();

    return 0;
}