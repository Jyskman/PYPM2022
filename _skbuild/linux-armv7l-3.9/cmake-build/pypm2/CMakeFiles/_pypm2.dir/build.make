# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/lib/python3.9/dist-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /usr/local/lib/python3.9/dist-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/Documents/PYPM2022

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build

# Include any dependencies generated for this target.
include pypm2/CMakeFiles/_pypm2.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include pypm2/CMakeFiles/_pypm2.dir/compiler_depend.make

# Include the progress variables for this target.
include pypm2/CMakeFiles/_pypm2.dir/progress.make

# Include the compile flags for this target's objects.
include pypm2/CMakeFiles/_pypm2.dir/flags.make

pypm2/CMakeFiles/_pypm2.dir/_pypm2.cxx.o: pypm2/CMakeFiles/_pypm2.dir/flags.make
pypm2/CMakeFiles/_pypm2.dir/_pypm2.cxx.o: ../../../pypm2/_pypm2.cxx
pypm2/CMakeFiles/_pypm2.dir/_pypm2.cxx.o: pypm2/CMakeFiles/_pypm2.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object pypm2/CMakeFiles/_pypm2.dir/_pypm2.cxx.o"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT pypm2/CMakeFiles/_pypm2.dir/_pypm2.cxx.o -MF CMakeFiles/_pypm2.dir/_pypm2.cxx.o.d -o CMakeFiles/_pypm2.dir/_pypm2.cxx.o -c /home/pi/Documents/PYPM2022/pypm2/_pypm2.cxx

pypm2/CMakeFiles/_pypm2.dir/_pypm2.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/_pypm2.dir/_pypm2.cxx.i"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/Documents/PYPM2022/pypm2/_pypm2.cxx > CMakeFiles/_pypm2.dir/_pypm2.cxx.i

pypm2/CMakeFiles/_pypm2.dir/_pypm2.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/_pypm2.dir/_pypm2.cxx.s"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/Documents/PYPM2022/pypm2/_pypm2.cxx -o CMakeFiles/_pypm2.dir/_pypm2.cxx.s

pypm2/CMakeFiles/_pypm2.dir/test.cxx.o: pypm2/CMakeFiles/_pypm2.dir/flags.make
pypm2/CMakeFiles/_pypm2.dir/test.cxx.o: ../../../pypm2/test.cxx
pypm2/CMakeFiles/_pypm2.dir/test.cxx.o: pypm2/CMakeFiles/_pypm2.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object pypm2/CMakeFiles/_pypm2.dir/test.cxx.o"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT pypm2/CMakeFiles/_pypm2.dir/test.cxx.o -MF CMakeFiles/_pypm2.dir/test.cxx.o.d -o CMakeFiles/_pypm2.dir/test.cxx.o -c /home/pi/Documents/PYPM2022/pypm2/test.cxx

pypm2/CMakeFiles/_pypm2.dir/test.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/_pypm2.dir/test.cxx.i"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/Documents/PYPM2022/pypm2/test.cxx > CMakeFiles/_pypm2.dir/test.cxx.i

pypm2/CMakeFiles/_pypm2.dir/test.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/_pypm2.dir/test.cxx.s"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/Documents/PYPM2022/pypm2/test.cxx -o CMakeFiles/_pypm2.dir/test.cxx.s

pypm2/CMakeFiles/_pypm2.dir/PY_PM.cxx.o: pypm2/CMakeFiles/_pypm2.dir/flags.make
pypm2/CMakeFiles/_pypm2.dir/PY_PM.cxx.o: ../../../pypm2/PY_PM.cxx
pypm2/CMakeFiles/_pypm2.dir/PY_PM.cxx.o: pypm2/CMakeFiles/_pypm2.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object pypm2/CMakeFiles/_pypm2.dir/PY_PM.cxx.o"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT pypm2/CMakeFiles/_pypm2.dir/PY_PM.cxx.o -MF CMakeFiles/_pypm2.dir/PY_PM.cxx.o.d -o CMakeFiles/_pypm2.dir/PY_PM.cxx.o -c /home/pi/Documents/PYPM2022/pypm2/PY_PM.cxx

pypm2/CMakeFiles/_pypm2.dir/PY_PM.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/_pypm2.dir/PY_PM.cxx.i"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/Documents/PYPM2022/pypm2/PY_PM.cxx > CMakeFiles/_pypm2.dir/PY_PM.cxx.i

pypm2/CMakeFiles/_pypm2.dir/PY_PM.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/_pypm2.dir/PY_PM.cxx.s"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/Documents/PYPM2022/pypm2/PY_PM.cxx -o CMakeFiles/_pypm2.dir/PY_PM.cxx.s

# Object files for target _pypm2
_pypm2_OBJECTS = \
"CMakeFiles/_pypm2.dir/_pypm2.cxx.o" \
"CMakeFiles/_pypm2.dir/test.cxx.o" \
"CMakeFiles/_pypm2.dir/PY_PM.cxx.o"

# External object files for target _pypm2
_pypm2_EXTERNAL_OBJECTS =

pypm2/_pypm2.cpython-39-arm-linux-gnueabihf.so: pypm2/CMakeFiles/_pypm2.dir/_pypm2.cxx.o
pypm2/_pypm2.cpython-39-arm-linux-gnueabihf.so: pypm2/CMakeFiles/_pypm2.dir/test.cxx.o
pypm2/_pypm2.cpython-39-arm-linux-gnueabihf.so: pypm2/CMakeFiles/_pypm2.dir/PY_PM.cxx.o
pypm2/_pypm2.cpython-39-arm-linux-gnueabihf.so: pypm2/CMakeFiles/_pypm2.dir/build.make
pypm2/_pypm2.cpython-39-arm-linux-gnueabihf.so: pypm2/CMakeFiles/_pypm2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared module _pypm2.cpython-39-arm-linux-gnueabihf.so"
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/_pypm2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
pypm2/CMakeFiles/_pypm2.dir/build: pypm2/_pypm2.cpython-39-arm-linux-gnueabihf.so
.PHONY : pypm2/CMakeFiles/_pypm2.dir/build

pypm2/CMakeFiles/_pypm2.dir/clean:
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 && $(CMAKE_COMMAND) -P CMakeFiles/_pypm2.dir/cmake_clean.cmake
.PHONY : pypm2/CMakeFiles/_pypm2.dir/clean

pypm2/CMakeFiles/_pypm2.dir/depend:
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/Documents/PYPM2022 /home/pi/Documents/PYPM2022/pypm2 /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2 /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/pypm2/CMakeFiles/_pypm2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : pypm2/CMakeFiles/_pypm2.dir/depend

