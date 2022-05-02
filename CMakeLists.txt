project(nlp_cpp)

cmake_minimum_required(VERSION 3.16)

set(CXX_STANDARD 20)

include_directories(${CMAKE_SOURCE_DIR}/lib/spacy-cpp/include
/usr/include/python3.8/)

set(SOURCES ${CMAKE_SOURCE_DIR}/src/main.cpp)

link_directories(${CMAKE_SOURCE_DIR}/lib/spacy-cpp/lib/)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCES})
target_link_libraries(${CMAKE_PROJECT_NAME} -lspacy)