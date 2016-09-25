#!/usr/bin/env bats

source ../libexec/pyoffline-clone

@test "Test pyenv download." {
    download_pyenv
    [ -d pyenv ]
    [ -d pyenv/cache ]
    rm -rf ./pyenv
}

@test "Test interpreter download." {
    local pyscript="../libexec/download_python.py"
    python ${pyscript}
    [ -d py_versions ]
    n=$(find ./ -name Python-*.tar.gz | wc -l)
    [ "$n" -eq 2 ]
    rm -rf ./py_versions
}

