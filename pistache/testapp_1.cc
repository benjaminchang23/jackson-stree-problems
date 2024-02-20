/*
based on: https://github.com/pistacheio/pistache/blob/master/examples/rest_description.cc
*/

#include <pistache/description.h>
#include <pistache/endpoint.h>
#include <pistache/http.h>

namespace testapp_1 {

namespace Generic
{

    void handleReady(const Pistache::Rest::Request&, Pistache::Http::ResponseWriter response)
    {
        response.send(Pistache::Http::Code::Ok, "1");
    }

}

class TestApp
{
public:
    TestApp(Pistache::Address addr)
        : httpEndpoint(std::make_shared<Pistache::Http::Endpoint>(addr))
        , desc("Banking API", "0.1")
    { }

    void init(size_t thr = 2)
    {
        auto opts = Pistache::Http::Endpoint::options()
                        .threads(static_cast<int>(thr));
        httpEndpoint->init(opts);
        createDescription();
    }

    void start()
    {
        router.initFromDescription(desc);

        // Pistache::Rest::Swagger swagger(desc);
        // swagger
        //     .uiPath("/doc")
        //     .uiDirectory("/home/octal/code/web/swagger-ui-2.1.4/dist")
        //     .apiPath("/banker-api.json")
        //     // .serializer(&Pistache::Rest::Serializer::rapidJson)
        //     .install(router);

        httpEndpoint->setHandler(router.handler());
        httpEndpoint->serve();
    }

private:
    void createDescription()
    {
        desc
            .info()
            .license("Apache", "http://www.apache.org/licenses/LICENSE-2.0");

        auto backendErrorResponse = desc.response(Pistache::Http::Code::Internal_Server_Error, "An error occured with the backend");

        desc
            .schemes(Pistache::Rest::Scheme::Http)
            .basePath("/v1")
            .produces(MIME(Application, Json))
            .consumes(MIME(Application, Json));

        desc
            .route(desc.get("/ready"))
            .bind(&Generic::handleReady)
            .response(Pistache::Http::Code::Ok, "Response to the /ready call")
            .hide();

        auto versionPath = desc.path("/v1");

        auto accountsPath = versionPath.path("/accounts");

        accountsPath
            .route(desc.get("/all"))
            .bind(&TestApp::retrieveAllAccounts, this)
            .produces(MIME(Application, Json), MIME(Application, Xml))
            .response(Pistache::Http::Code::Ok, "The list of all account");

        accountsPath
            .route(desc.get("/:name"), "Retrieve an account")
            .bind(&TestApp::retrieveAccount, this)
            .produces(MIME(Application, Json))
            .parameter<Pistache::Rest::Type::String>("name", "The name of the account to retrieve")
            .response(Pistache::Http::Code::Ok, "The requested account")
            .response(backendErrorResponse);

        accountsPath
            .route(desc.post("/:name"), "Create an account")
            .bind(&TestApp::createAccount, this)
            .produces(MIME(Application, Json))
            .consumes(MIME(Application, Json))
            .parameter<Pistache::Rest::Type::String>("name", "The name of the account to create")
            .response(Pistache::Http::Code::Ok, "The initial state of the account")
            .response(backendErrorResponse);

        auto accountPath = accountsPath.path("/:name");
        accountPath.parameter<Pistache::Rest::Type::String>("name", "The name of the account to operate on");

        accountPath
            .route(desc.post("/budget"), "Add budget to the account")
            .bind(&TestApp::creditAccount, this)
            .produces(MIME(Application, Json))
            .response(Pistache::Http::Code::Ok, "Budget has been added to the account")
            .response(backendErrorResponse);
    }

    void retrieveAllAccounts(const Pistache::Rest::Request&, Pistache::Http::ResponseWriter response)
    {
        response.send(Pistache::Http::Code::Ok, "No Account");
    }

    void retrieveAccount(const Pistache::Rest::Request&, Pistache::Http::ResponseWriter response)
    {
        response.send(Pistache::Http::Code::Ok, "The bank is closed, come back later");
    }

    void createAccount(const Pistache::Rest::Request&, Pistache::Http::ResponseWriter response)
    {
        response.send(Pistache::Http::Code::Ok, "The bank is closed, come back later");
    }

    void creditAccount(const Pistache::Rest::Request&, Pistache::Http::ResponseWriter response)
    {
        response.send(Pistache::Http::Code::Ok, "The bank is closed, come back later");
    }

    std::shared_ptr<Pistache::Http::Endpoint> httpEndpoint;
    Pistache::Rest::Description desc;
    Pistache::Rest::Router router;
};

} // namespace testapp_1

int main(int argc, char* argv[])
{
    Pistache::Port port(9080);

    int thr = 2;

    if (argc >= 2)
    {
        port = static_cast<uint16_t>(std::stol(argv[1]));

        if (argc == 3)
            thr = std::stoi(argv[2]);
    }

    Pistache::Address addr(Pistache::Ipv4::any(), port);

    std::cout << "Cores = " << Pistache::hardware_concurrency() << std::endl;
    std::cout << "Using " << thr << " threads" << std::endl;

    testapp_1::TestApp app(addr);

    app.init(thr);
    app.start();
}