add_executable(move_0 move_0.cc)
add_executable(move_1 move_1.cc)
add_executable(move_2 move_2.cc)
add_executable(move_3 move_3.cc)
add_executable(move_4 move_4.cc)
add_executable(templates_0 templates_0.cc)
add_executable(templates_1 templates_1.cc)
add_executable(templates_2 templates_2.cc)

install(TARGETS
    move_0
    move_1
    move_2
    move_3
    move_4
    templates_0
    templates_1
    templates_2
    RUNTIME DESTINATION bin
    )