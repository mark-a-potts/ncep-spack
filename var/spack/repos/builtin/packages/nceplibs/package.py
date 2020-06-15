# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install nceplibs
#
# You can edit this file again by typing:
#
#     spack edit nceplibs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Nceplibs(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://www.example.com/example-1.2.3.tar.gz"
    git      = "git@github.com:mark-a-potts/NCEPLIBS"

    # FIXME: Add proper versions and checksums here.
    version('v1.0.0',  branch='gsi-update', submodules=True)

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('netcdf')
    depends_on('netcdf-fortran')
    depends_on('hdf5')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DBUILD_FOR_GSI=ON']
        return args
