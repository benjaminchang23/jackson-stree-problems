#include <functional>
#include <iostream>

using some_callback = std::function<void(const std::string &name, size_t index)>;

class Widget
{
public:
    int RegisterCallback(const some_callback &callback)
    {
        callback_ = callback;
        return 0;
    }

    void DoCallback(const std::string &name, size_t index)
    {
        if (callback_)
            callback_(name, index);
    }

    some_callback callback_;
};

int main()
{
    Widget widget;

    widget.RegisterCallback(
        [&](const std::string &name, size_t index)
        {
            std::cout << name << " - " << index << std::endl;
        }
    );

    widget.DoCallback("name-0", 0);
    widget.DoCallback("name-1", 1);

    return 0;
}