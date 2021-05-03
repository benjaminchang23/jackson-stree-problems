#include <atomic>
#include <iostream>
#include <memory>

class AtomicWidget
{
public:
    AtomicWidget(bool done) :
        done_(done)
    {
    }

    AtomicWidget(const AtomicWidget &widget) :
        done_(bool(widget.done_))
    {
    }

    bool GetDone()
    {
        return done_;
    }

    void SetDone(bool done)
    {
        done_ = done;
    }

private:
    std::atomic_bool done_;
};

class Widget
{
public:
    Widget(bool done) :
        done_(done)
    {
    }

    Widget(const Widget &widget) :
        done_(widget.done_)
    {

    }

    bool GetDone()
    {
        return done_;
    }

    void SetDone(bool done)
    {
        done_ = done;
    }


private:
    bool done_;
};

int main()
{
    auto widget_ptr_0 = std::make_shared<Widget>(true);
    auto widget_ptr_1 = std::make_shared<Widget>(*widget_ptr_0);
    std::cout << "widget 0 done: " << widget_ptr_0->GetDone() << std::endl;
    std::cout << "widget 1 done: " << widget_ptr_1->GetDone() << std::endl;

    widget_ptr_0->SetDone(false);

    std::cout << "widget 0 done: " << widget_ptr_0->GetDone() << std::endl;
    std::cout << "widget 1 done: " << widget_ptr_1->GetDone() << std::endl;

    auto atomic_widget_ptr_0 = std::make_shared<AtomicWidget>(true);
    auto atomic_widget_ptr_1 = std::make_shared<AtomicWidget>(*atomic_widget_ptr_0);

    std::cout << "atomic widget 0 done: " << atomic_widget_ptr_0->GetDone() << std::endl;
    std::cout << "atomic widget 1 done: " << atomic_widget_ptr_1->GetDone() << std::endl;

    atomic_widget_ptr_0->SetDone(false);

    std::cout << "atomic widget 0 done: " << atomic_widget_ptr_0->GetDone() << std::endl;
    std::cout << "atomic widget 1 done: " << atomic_widget_ptr_1->GetDone() << std::endl;

    return 0;
}