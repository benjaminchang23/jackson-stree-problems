add_executable(move_0 move_0.cc)
add_executable(move_1 move_1.cc)
add_executable(move_2 move_2.cc)
add_executable(move_3 move_3.cc)
add_executable(templates_0 templates_0.cc)
add_executable(templates_1 templates_1.cc)
add_executable(templates_2 templates_2.cc)

add_executable(CAT_0 CAT_0.cc)

install(TARGETS
    CAT_0
    move_0
    move_1
    move_2
    move_3
    templates_0
    templates_1
    templates_2
    RUNTIME DESTINATION bin
    )