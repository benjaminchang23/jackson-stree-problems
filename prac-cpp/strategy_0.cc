#include <iostream>
#include <memory>
#include <sstream>
#include <string>

struct ParserInfo
{
    std::string title = "default-title";
    std::string author = "default-author";
    std::string content = "default-content";
};

inline std::ostream& operator << (std::ostream &out, const ParserInfo &parser_info)
{
    out << "title: " << parser_info.title << " ";
    out << "author: " << parser_info.author << " ";
    out << "content: " << parser_info.content;

    return out;
}

class ParserStrategy
{
public:
    virtual void GetTitle(ParserInfo &parser_info) const = 0;
    virtual void FindMetadata(ParserInfo &parser_info) const = 0;
    virtual void ParseSection(ParserInfo &parser_info) const = 0;
    virtual void SeekToContent(void) const = 0;
};

class DefaultParser : ParserStrategy
{
public:
    explicit DefaultParser()
    {

    }

    void GetTitle(ParserInfo &parser_info) const override
    {
        parser_info.title = "default-parser-title";

        return;
    }

    void FindMetadata(ParserInfo &parser_info) const override
    {
        parser_info.author = "default-parser-author";

        return;
    }

    void ParseSection(ParserInfo &parser_info) const override
    {
        parser_info.content = "default-parser-content";

        return;
    }

    void SeekToContent(void) const override
    {
        return;
    }
};

int main()
{
    auto parser_strat = std::make_shared<DefaultParser>();

    ParserInfo parser_info;

    parser_strat->FindMetadata(parser_info);
    parser_strat->GetTitle(parser_info);
    parser_strat->ParseSection(parser_info);

    std::cout << parser_info << std::endl;

    return 0;
}