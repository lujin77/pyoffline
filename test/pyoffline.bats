#!/usr/bin/env bats

source ../libexec/pyoffline

@test "Test pyenv downloading." {
    download_pyenv
    [ -d pyenv ]
    [ -d pyenv/cache ]
    rm -rf ./pyenv
}

