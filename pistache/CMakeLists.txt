# find_package(pistache REQUIRED)

set(SOURCES_LIST
    testapp_0.cc
)

string( REPLACE ".cc" "" BASENAMES_LIST "${SOURCES_LIST}" )
set( TARGETS_LIST ${BASENAMES_LIST} )
    
foreach( name ${TARGETS_LIST} )
    add_executable( ${name} ${name}.cc )
endforeach()

foreach( name ${TARGETS_LIST} )
    target_link_libraries(${name} PRIVATE pistache pthread)
endforeach()

foreach( name ${TARGETS_LIST} )
    install(TARGETS
        ${name}
        RUNTIME DESTINATION bin
    )
endforeach()
