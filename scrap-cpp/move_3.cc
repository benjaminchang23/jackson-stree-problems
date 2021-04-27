#include <iostream>
#include <memory>
#include <vector>

template<typename T>
void PrintVector(const std::vector<T> &vec)
{
    for (auto element : vec)
    {
        std::cout << element << " ";
    }

    std::cout << std::endl;
}

template<typename T, typename Arg>
std::shared_ptr<T> factory_0(Arg arg)
{
    return std::shared_ptr<T>(new T(arg));
}

template<typename T, typename Arg>
std::shared_ptr<T> factory_1(Arg &arg)
{
    return std::shared_ptr<T>(new T(arg));
}

template<typename T, typename Arg>
std::shared_ptr<T> factory_2(const Arg &arg)
{
    return std::shared_ptr<T>(new T(arg));
}

template<typename T, typename Arg>
std::shared_ptr<T> factory_3(Arg &&arg)
{
    return std::shared_ptr<T>(new T(std::forward<Arg>(arg)));
}

class IntContainer
{
public:
    IntContainer(int i)
    {
        vec_.emplace_back(i);
    }

    IntContainer(int i, int j)
    {
        vec_.emplace_back(i);
        vec_.emplace_back(j);
    }

    void PrintContents()
    {
        PrintVector<int>(vec_);
    }

private:
    std::vector<int> vec_;
};

IntContainer Foo()
{
    return IntContainer(2);
}

int main()
{
    // factory_0 produces an extra call by value
    factory_0<int>(1);
    factory_0<IntContainer>(Foo());

    // factory_1 can't be called on rvalues only lvalues
    int i = 1;
    auto res = Foo();

    factory_1<IntContainer>(i);
    factory_1<IntContainer>(res);

    // factory_2 can do both, but since it needs a const reference it can't use move(or more than 1 argument)
    factory_2<IntContainer>(1);
    factory_2<IntContainer>(Foo());
    factory_2<IntContainer>(i);
    factory_2<IntContainer>(res);

    factory_3<IntContainer>(1);
    factory_3<IntContainer>(Foo());
    factory_3<IntContainer>(i);
    factory_3<IntContainer>(res);

    return 0;
}