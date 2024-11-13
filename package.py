name = "hdf5"

version = "1.13.0"

description = \
    """
    HDF5 file management system
    """

variants = [["platform-linux", "arch-x86_64"]]

uuid = "repository.hdf5"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")
