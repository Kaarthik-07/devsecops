{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  packages = with pkgs; [
    pyenv
    python313

    gcc
    gnumake
    pkg-config
    zlib
    openssl
    readline
    sqlite
    xz
    bzip2
    libffi
    tk

    git
    curl
    wget
  ];

  shellHook = ''
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"

    # Runtime libraries required by Python's scientific packages
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:${pkgs.openssl}/lib''${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

    eval "$(pyenv init -)"

    echo "Data Foundations environment ready"
    pyenv --version
  '';
}
