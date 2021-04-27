#include <iostream>
#include <vector>

struct DrillFile
{
    float x;
    float y;
    float z;

    int ObjType;
};

class DrillObjectDataStorage
{
public:
    DrillObjectDataStorage() :
        vec_()
    {

    }

    void AddFile(const DrillFile &file)
    {
        vec_.emplace_back(file);
    }

    void PrintFiles()
    {
        for (auto element : vec_)
        {
            std::cout << element.x << " " << element.y << " " << element.z << " " << element.ObjType << std::endl;
        }
        // consider cuda, kernal code, hardware accel
    }

private:
    std::vector<DrillFile> vec_;
};

int main()
{
    DrillFile file;

    file.x = 1.0;
    file.y = 2.0;
    file.z = 3.0;

    file.ObjType = 0;

    auto drill = DrillObjectDataStorage();

    drill.AddFile(file);

    drill.PrintFiles();

    return 0;
}