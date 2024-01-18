set(OPENSSL_USE_STATIC_LIBS TRUE)
find_package(OpenSSL REQUIRED)

set(SOURCES_LIST
    bool_print_0.cc
    char_print_0.cc
    char_print_1.cc
    chrono_0.cc
    copy_ctor_0.cc
    copy_ctor_1.cc
    enum_class_0.cc
    for_loop_0.cc
    function_order_0.cc
    hash_gen_0.cc
    hash_gen_1.cc
    lambda_0.cc
    lambda_1.cc
    map_address_0.cc
    memcpy_0.cc
    move_0.cc
    move_1.cc
    move_2.cc
    move_3.cc
    pragma_push_pop_0.cc
    pointer_0.cc
    pointer_1.cc
    printable_0.cc
    shared_pointer_0.cc
    strings_0.cc
    strings_1.cc
    stringstream_0.cc
    struct_overload_0.cc
    struct_overload_1.cc
    struct_overload_2.cc
    struct_overload_3.cc
    templates_0.cc
    templates_1.cc
    templates_2.cc
    templates_3.cc
    time_0.cc
    unicode_0.cc
)

string( REPLACE ".cc" "" BASENAMES_LIST "${SOURCES_LIST}" )
set( TARGETS_LIST ${BASENAMES_LIST} )
    
foreach( name ${TARGETS_LIST} )
    add_executable( ${name} ${name}.cc )
endforeach()

target_link_libraries(hash_gen_0 OpenSSL::SSL)
target_link_libraries(hash_gen_1 OpenSSL::SSL)

foreach( name ${TARGETS_LIST} )
    install(TARGETS
        ${name}
        RUNTIME DESTINATION bin
    )
endforeach()
