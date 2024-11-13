CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(hdf5_version ${HDF5_VERSION})

# set(url_hdf5 https://www.hdfgroup.org/ftp/HDF5/releases/hdf5-${hdf5_version}/src/hdf5-${hdf5_version}.tar.gz)
set(url_hdf5 https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.14/src/hdf5-1.8.14.tar.gz)
set(tag_hdf5 ${hdf5_version})

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    hdf5
    URL ${url_hdf5}
    PREFIX hdf5
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-pic --enable-production --disable-debug --enable-threadsafe --with-pthread=/usr/include,/usr/lib
    BUILD_COMMAND make
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
)

rez_install_files(
    cmake/hdf5.cmake
    DESTINATION .
)
