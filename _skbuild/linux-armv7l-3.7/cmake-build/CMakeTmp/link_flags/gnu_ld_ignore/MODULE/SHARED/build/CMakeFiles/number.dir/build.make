# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build

# Include any dependencies generated for this target.
include CMakeFiles/number.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/number.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/number.dir/flags.make

CMakeFiles/number.dir/number.c.o: CMakeFiles/number.dir/flags.make
CMakeFiles/number.dir/number.c.o: /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src/number.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --progress-dir=/home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/number.dir/number.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/number.dir/number.c.o   -c /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src/number.c

CMakeFiles/number.dir/number.c.i: cmake_force
	@echo "Preprocessing C source to CMakeFiles/number.dir/number.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src/number.c > CMakeFiles/number.dir/number.c.i

CMakeFiles/number.dir/number.c.s: cmake_force
	@echo "Compiling C source to assembly CMakeFiles/number.dir/number.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src/number.c -o CMakeFiles/number.dir/number.c.s

# Object files for target number
number_OBJECTS = \
"CMakeFiles/number.dir/number.c.o"

# External object files for target number
number_EXTERNAL_OBJECTS =

libnumber.so: CMakeFiles/number.dir/number.c.o
libnumber.so: CMakeFiles/number.dir/build.make
libnumber.so: CMakeFiles/number.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --progress-dir=/home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared library libnumber.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/number.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/number.dir/build: libnumber.so

.PHONY : CMakeFiles/number.dir/build

CMakeFiles/number.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/number.dir/cmake_clean.cmake
.PHONY : CMakeFiles/number.dir/clean

CMakeFiles/number.dir/depend:
	cd /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/src /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build /home/pi/Documents/Projects/PYPM_Python3_v2/_skbuild/linux-armv7l-3.7/cmake-build/CMakeTmp/link_flags/gnu_ld_ignore/MODULE/SHARED/build/CMakeFiles/number.dir/DependInfo.cmake
.PHONY : CMakeFiles/number.dir/depend

