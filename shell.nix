{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  packages = with pkgs; [
    python313
    python313Packages.pip

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
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:${pkgs.openssl}/lib''${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

    echo "Data Foundations environment ready"
    python3 --version
    python3 -m pip --version
  '';
}
