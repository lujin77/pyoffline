#!/usr/bin/env bats

source ../libexec/pyoffline-clone

@test "Test pyenv download." {
    download_pyenv
    [ -d pyenv ]
    [ -d pyenv/cache ]
    rm -rf ./pyenv
}

@test "Test python download." {
    local pyscript="../libexec/download_python.py"
    python ${pyscript}
    [ -d py_versions ]
    n=$(find ./ -name Python-*.tar.gz | wc -l)
    [ "$n" -eq 2 ]
    rm -rf ./py_versions
}

@test "Test python packages download." {
    local pyscript="../libexec/download_packages.py"
    local pyv=$(python -c 'import platform; print(platform.python_version())')
    python ${pyscript}
    [ -d py_packages ]
    [ -d "py_packages/${pyv}" ]
    n=$(ls "py_packages/${pyv}" | wc -l)
    [ "$n" -ne 0 ]
    rm -rf ./py_packages
}

