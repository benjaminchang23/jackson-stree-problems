#include <atomic>
#include <iostream>
#include <memory>
#include <utility>

class AtomicWidget
{
public:
    AtomicWidget(bool done) :
        done_(done)
    {
    }

    // atomic has a deleted copy constructor, which means we have to make one of our own
    AtomicWidget(const AtomicWidget &widget) :
        done_(bool(widget.done_))
    {
    }

    virtual bool GetDone()
    {
        return done_;
    }

    void SetDone(bool done)
    {
        done_ = done;
    }

protected:
    std::atomic_bool done_;
};

class AtomicWidgetWithPrintout : public AtomicWidget
{
public:
    AtomicWidgetWithPrintout(bool done) :
        AtomicWidget(done)
    {
    }

    AtomicWidgetWithPrintout(const AtomicWidgetWithPrintout &widget) :
        AtomicWidget(widget)
    {
    }

    bool GetDone()
    {
        std::cout << "Derived class print" << std::endl;
        return done_;
    }

};

int main()
{
    auto atomic_widget_ptr_0 = std::make_shared<AtomicWidgetWithPrintout>(true);
    auto atomic_widget_ptr_1 = std::make_shared<AtomicWidget>(*atomic_widget_ptr_0);
    std::shared_ptr<AtomicWidget> normal_widget;

    normal_widget = std::static_pointer_cast<AtomicWidget>(atomic_widget_ptr_1);

    std::cout << "atomic widget static pointer cast done: " << normal_widget->GetDone() << std::endl;

    std::cout << "atomic widget 0 done: " << atomic_widget_ptr_0->GetDone() << std::endl;
    std::cout << "atomic widget 1 done: " << atomic_widget_ptr_1->GetDone() << std::endl;

    atomic_widget_ptr_0->SetDone(false);

    std::cout << "atomic widget 0 done: " << atomic_widget_ptr_0->GetDone() << std::endl;
    std::cout << "atomic widget 1 done: " << atomic_widget_ptr_1->GetDone() << std::endl;

    return 0;
}