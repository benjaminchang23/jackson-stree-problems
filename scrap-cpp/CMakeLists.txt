add_executable(move_0 move_0)
add_executable(templates_0 templates_0.cc)
add_executable(templates_1 templates_1.cc)

install(TARGETS
    move_0
    templates_0
    templates_1
    RUNTIME DESTINATION bin
    )