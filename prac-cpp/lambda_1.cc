#include <functional>
#include <iostream>
#include <sstream>

using some_callback = std::function<std::string(const std::string &name, size_t index)>;

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
        std::string output;

        if (callback_)
            output = callback_(name, index);

        std::cout << output << std::endl;
    }

    some_callback callback_;
};

int main()
{
    Widget widget;

    widget.RegisterCallback(
        [&](const std::string &name, size_t index)
        {
            std::stringstream ss;
            ss << name << " - " << index;
            return ss.str();
        }
    );

    widget.DoCallback("name-0", 0);
    widget.DoCallback("name-1", 1);

    return 0;
}