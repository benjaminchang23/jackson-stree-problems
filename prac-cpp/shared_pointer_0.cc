#include <iostream>
#include <memory>

class TinyClass {

public:
    explicit TinyClass(int i) :
    i(i)
    {}

    int GetTiny()
    {
        return i;
    }
private:
    int i;
};

class MyClass {
private:
    std::shared_ptr<TinyClass> tiny_class;

public:
    // Constructor taking a shared pointer to int
    explicit MyClass(const std::shared_ptr<TinyClass> &tiny_class) : tiny_class(tiny_class) {}

    void display() {
        if (tiny_class) {
            std::cout << "Value from tiny class: " << tiny_class->GetTiny() << std::endl;
        } else {
            std::cout << "Shared pointer is null." << std::endl;
        }
    }
};

int main() {
    // Create a shared pointer to an int
    auto tiny_class = std::make_shared<TinyClass>(42);

    // Create an instance of MyClass with the shared pointer
    MyClass myObj(tiny_class);

    // Display the value using the MyClass instance
    myObj.display();

    return 0;
}
