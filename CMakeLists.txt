 
cmake_minimum_required(VERSION 3.5.0)

project(pypm2)

find_package(PythonExtensions REQUIRED)

add_subdirectory(pypm2)

file(WRITE "${CMAKE_BINARY_DIR}/pypmModule.py" "# pypmModule.py")
install(FILES "${CMAKE_BINARY_DIR}/pypmModule.py" DESTINATION ".")

#
# This code is here *ONLY* to test that the different signatures of
# "check_dynamic_lookup" functions are not causing errors.
#
include(targetLinkLibrariesWithDynamicLookup)
check_dynamic_lookup("MODULE" "SHARED" "PYPM_HAS_DYNAMIC_LOOKUP")
check_dynamic_lookup("PYPM_HAS_DYNAMIC_LOOKUP")
