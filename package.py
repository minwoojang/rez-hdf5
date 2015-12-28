name = "hdf5"

version = "1.8.14"

description = \
    """
    alembic
    """

variants = [
    ["platform-linux"]
]

uuid = "repository.hdf5"

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.LD_LIBRARY_PATH.append("{root}/lib")
