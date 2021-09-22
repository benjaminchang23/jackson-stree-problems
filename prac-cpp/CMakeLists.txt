add_executable(copy_ctor_0 copy_ctor_0.cc)
add_executable(copy_ctor_1 copy_ctor_1.cc)
add_executable(function_order_0 function_order_0.cc)
add_executable(map_address_0 map_address_0.cc)
add_executable(move_0 move_0.cc)
add_executable(move_1 move_1.cc)
add_executable(move_2 move_2.cc)
add_executable(move_3 move_3.cc)
add_executable(strings_0 strings_0.cc)
add_executable(struct_overload_0 struct_overload_0.cc)
add_executable(struct_overload_1 struct_overload_1.cc)
add_executable(struct_overload_2 struct_overload_2.cc)
add_executable(struct_overload_3 struct_overload_3.cc)
add_executable(templates_0 templates_0.cc)
add_executable(templates_1 templates_1.cc)
add_executable(templates_2 templates_2.cc)
add_executable(time_0 time_0.cc)
add_executable(unicode_0 unicode_0.cc)

install(TARGETS
    copy_ctor_0
    copy_ctor_1
    function_order_0
    map_address_0
    move_0
    move_1
    move_2
    move_3
    strings_0
    struct_overload_0
    struct_overload_1
    struct_overload_2
    struct_overload_3
    templates_0
    templates_1
    templates_2
    time_0
    unicode_0
    RUNTIME DESTINATION bin
    )
