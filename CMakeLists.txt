cmake_minimum_required(VERSION 3.0.0)
project(Dem1 VERSION 0.1.0)

include(CTest)
enable_testing()

# aux_source_directory(./other OTHER_DIR)
# add_executable(Dem1 ${OTHER_DIR})

add_executable(main test.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)


