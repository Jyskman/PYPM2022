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
CMAKE_SOURCE_DIR = /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build

# Include any dependencies generated for this target.
include CMakeFiles/counter.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/counter.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/counter.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/counter.dir/flags.make

CMakeFiles/counter.dir/counter.c.o: CMakeFiles/counter.dir/flags.make
CMakeFiles/counter.dir/counter.c.o: /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src/counter.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --progress-dir=/home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/counter.dir/counter.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/counter.dir/counter.c.o -c /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src/counter.c

CMakeFiles/counter.dir/counter.c.i: cmake_force
	@echo "Preprocessing C source to CMakeFiles/counter.dir/counter.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src/counter.c > CMakeFiles/counter.dir/counter.c.i

CMakeFiles/counter.dir/counter.c.s: cmake_force
	@echo "Compiling C source to assembly CMakeFiles/counter.dir/counter.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src/counter.c -o CMakeFiles/counter.dir/counter.c.s

# Object files for target counter
counter_OBJECTS = \
"CMakeFiles/counter.dir/counter.c.o"

# External object files for target counter
counter_EXTERNAL_OBJECTS =

counter.so: CMakeFiles/counter.dir/counter.c.o
counter.so: CMakeFiles/counter.dir/build.make
counter.so: CMakeFiles/counter.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --progress-dir=/home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared module counter.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/counter.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/counter.dir/build: counter.so
.PHONY : CMakeFiles/counter.dir/build

CMakeFiles/counter.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/counter.dir/cmake_clean.cmake
.PHONY : CMakeFiles/counter.dir/clean

CMakeFiles/counter.dir/depend:
	cd /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build /home/pi/Documents/PYPM2022/_skbuild/linux-armv7l-3.9/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build/CMakeFiles/counter.dir/DependInfo.cmake
.PHONY : CMakeFiles/counter.dir/depend
