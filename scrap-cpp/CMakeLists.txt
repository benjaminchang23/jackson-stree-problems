add_executable(templates_0 templates_0.cc)
add_executable(templates_1 templates_1.cc)

install(TARGETS
    templates_0
    templates_1
    RUNTIME DESTINATION bin
    )