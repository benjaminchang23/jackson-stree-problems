
set(SOURCES_LIST
    round-b-1-final.cc
    round-b-1.cc
)

string( REPLACE ".cc" "" BASENAMES_LIST "${SOURCES_LIST}" )
set( TARGETS_LIST ${BASENAMES_LIST} )
    
foreach( name ${TARGETS_LIST} )
    add_executable( ${name} ${name}.cc )
endforeach()

foreach( name ${TARGETS_LIST} )
    install(TARGETS
        ${name}
        RUNTIME DESTINATION bin
    )
endforeach()
