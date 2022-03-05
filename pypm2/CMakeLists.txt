
add_library(_pypm2 MODULE _pypm2.cxx test.cxx PY_PM.cxx)
python_extension_module(_pypm2)

install(TARGETS _pypm2 LIBRARY DESTINATION pypm2)

set(world "${CMAKE_CURRENT_SOURCE_DIR}/world.py")
file(WRITE ${world} "")

install(FILES ${world} DESTINATION pypm2)
