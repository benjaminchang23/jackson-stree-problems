add_executable(move_0 move_0.cc)
add_executable(move_1 move_1.cc)
add_executable(move_2 move_2.cc)
add_executable(templates_0 templates_0.cc)
add_executable(templates_1 templates_1.cc)

install(TARGETS
    move_0
    move_1
    move_2
    templates_0
    templates_1
    RUNTIME DESTINATION bin
    )