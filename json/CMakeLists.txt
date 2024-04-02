
set(SOURCES_LIST
    json_0.cc
    json_1.cc
    json_2.cc
    json_3.cc
    json_4.cc
    json_5.cc
    json_6.cc
    json_from_str_0.cc
)

string( REPLACE ".cc" "" BASENAMES_LIST "${SOURCES_LIST}" )
set( TARGETS_LIST ${BASENAMES_LIST} )
    
foreach( name ${TARGETS_LIST} )
    add_executable( ${name} ${name}.cc )
    target_link_libraries( ${name} PRIVATE nlohmann_json::nlohmann_json)
endforeach()

foreach( name ${TARGETS_LIST} )
    install(TARGETS
        ${name}
        RUNTIME DESTINATION bin
    )
endforeach()
