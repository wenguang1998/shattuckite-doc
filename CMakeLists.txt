project(shattuckitedoc)
cmake_minimum_required(VERSION 3.5)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMakeModule)

include(ShattuckiteSphinx)

ShattuckiteSphinxDoc(SDP 001 ${CMAKE_SOURCE_DIR}/projectPlan ${CMAKE_BINARY_DIR})
ShattuckiteSphinxDoc(PRD 002 ${CMAKE_SOURCE_DIR}/requirments ${CMAKE_BINARY_DIR})
ShattuckiteSphinxDoc(SDD 003 ${CMAKE_SOURCE_DIR}/architectureDesign ${CMAKE_BINARY_DIR})


add_custom_target(run ALL
    DEPENDS ${CMAKE_BINARY_DIR}/shattuckite-SDP.pdf
            ${CMAKE_BINARY_DIR}/shattuckite-PRD.pdf
            ${CMAKE_BINARY_DIR}/shattuckite-SDD.pdf
            ${CMAKE_BINARY_DIR}/shattuckite-SDP-html
            ${CMAKE_BINARY_DIR}/shattuckite-PRD-html
            ${CMAKE_BINARY_DIR}/shattuckite-SDD-html
    )


