#include <deque>
#include <iostream>
#include <mutex>

template <typename T>
void PrintDeque(const std::deque<T> &deque)
{
    for (auto element : deque)
    {
        std::cout << element << " ";
    }

    std::cout << std::endl;
}

template <typename T>
class Widget
{
public:
    Widget()
    {}

    Widget(Widget &&rhs)
        : deque_(std::move(rhs.deque_))
    {
        std::cout << "moved" << std::endl;
    }

    decltype(auto) emplace_back(const T &element)
    {
        return deque_.emplace_back(element);
    }

    void ReadDeque()
    {
        PrintDeque(deque_);
    }

    size_t size()
    {
        return deque_.size();
    }

private:
    std::deque<T> deque_;
};

int main()
{
    auto wid = Widget<int>();

    wid.emplace_back(10);
    wid.emplace_back(120);
    wid.emplace_back(1230);

    wid.ReadDeque();

}