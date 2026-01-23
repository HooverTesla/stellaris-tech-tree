let
  pkgs = import (fetchTarball("https://github.com/NixOS/nixpkgs/archive/929116e316068c7318c54eb4d827f7d9756d5e9c.tar.gz")) {};
  buildInputs = (with pkgs; [
    jekyll
    python3
    python3Packages.pip
    python3Packages.imageio
    python3Packages.pillow
  ]);
in
pkgs.mkShell {
  inherit buildInputs;
}
