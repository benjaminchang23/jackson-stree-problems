#include <cstdint>
#include <memory>

#include <pistache/endpoint.h>
#include <pistache/http.h>
#include <pistache/mime.h>
#include <pistache/net.h>
#include <pistache/router.h>

namespace testapp_0 {

class TestApp
{
public:
    TestApp(uint16_t port_number = 8000, uint16_t num_threads = 4) :
        port_number_(port_number),
        num_threads_(num_threads),
        address_("localhost", port_number),
        endpoint_(std::make_shared<Pistache::Http::Endpoint>(address_)),
        rest_router_()
    {
    }

    void run();

private:

    int SetRoutes();

    void CreateEntry(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void ReadEntry(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void UpdateEntry(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void DeleteEntry(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);

    uint16_t port_number_;
    uint16_t num_threads_;
    Pistache::Address address_;
    std::shared_ptr<Pistache::Http::Endpoint> endpoint_;
    Pistache::Rest::Router rest_router_;
};

int TestApp::SetRoutes()
{
    Pistache::Rest::Routes::Put(rest_router_, "/work_entry/:uuid", Pistache::Rest::Routes::bind(&TestApp::CreateEntry, this));
    Pistache::Rest::Routes::Post(rest_router_, "/work_entry/:uuid", Pistache::Rest::Routes::bind(&TestApp::CreateEntry, this));
    Pistache::Rest::Routes::Get(rest_router_, "/work_entry/:uuid", Pistache::Rest::Routes::bind(&TestApp::ReadEntry, this));
    Pistache::Rest::Routes::Put(rest_router_, "/work_entry/:uuid", Pistache::Rest::Routes::bind(&TestApp::UpdateEntry, this));
    Pistache::Rest::Routes::Delete(rest_router_, "/work_entry/:uuid", Pistache::Rest::Routes::bind(&TestApp::DeleteEntry, this));

    return 0;
}

void TestApp::CreateEntry(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response)
{
    try
    {
        const std::string json = request.body();
        const std::string resource = request.param(":uuid").as<std::string>();
        response.send(Pistache::Http::Code::Ok, "work_entry " + resource + " created.", MIME(Text, Plain));
    }
    catch (const std::runtime_error &ex)
    {
        response.send(Pistache::Http::Code::Not_Found, ex.what(), MIME(Text, Plain));
    }
    catch (...)
    {
        response.send(Pistache::Http::Code::Internal_Server_Error, "Internal error", MIME(Text, Plain));
    }
}

void TestApp::ReadEntry(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response)
{
    try
    {
        const std::string json = request.body();
        const std::string resource = request.param(":uuid").as<std::string>();
        response.send(Pistache::Http::Code::Ok, "work_entry " + resource + " read.", MIME(Text, Plain));
    }
    catch (const std::runtime_error &ex)
    {
        response.send(Pistache::Http::Code::Not_Found, ex.what(), MIME(Text, Plain));
    }
    catch (...)
    {
        response.send(Pistache::Http::Code::Internal_Server_Error, "Internal error", MIME(Text, Plain));
    }
}

void TestApp::UpdateEntry(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response)
{
    try
    {
        const std::string json = request.body();
        const std::string resource = request.param(":uuid").as<std::string>();
        response.send(Pistache::Http::Code::Ok, "work_entry " + resource + " updated.", MIME(Text, Plain));
    }
    catch (const std::runtime_error &ex)
    {
        response.send(Pistache::Http::Code::Not_Found, ex.what(), MIME(Text, Plain));
    }
    catch (...)
    {
        response.send(Pistache::Http::Code::Internal_Server_Error, "Internal error", MIME(Text, Plain));
    }
}

void TestApp::DeleteEntry(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response)
{
    try
    {
        const std::string json = request.body();
        const std::string resource = request.param(":uuid").as<std::string>();
        response.send(Pistache::Http::Code::Ok, "work_entry " + resource + " deleted.", MIME(Text, Plain));
    }
    catch (const std::runtime_error &ex)
    {
        response.send(Pistache::Http::Code::Not_Found, ex.what(), MIME(Text, Plain));
    }
    catch (...)
    {
        response.send(Pistache::Http::Code::Internal_Server_Error, "Internal error", MIME(Text, Plain));
    }
}

void TestApp::run()
{
    std::cout << "Starting on port " << port_number_ << " with " << num_threads_ << " threads." << std::endl;
    endpoint_->init(Pistache::Http::Endpoint::options().threads(num_threads_));
    SetRoutes();
    endpoint_->setHandler(rest_router_.handler());
    endpoint_->serve();
}

} // namespace testapp_0

int main()
{
    testapp_0::TestApp app;
    app.run();

    return 0;
}