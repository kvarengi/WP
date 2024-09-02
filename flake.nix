{
  description = "Binary options bot flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    pkgs = import nixpkgs {
      system = "x86_64-linux";
      config.allowUnfree = true;
    };
  in
    with pkgs; {
      devShells.x86_64-linux.default = mkShell {
        name = "Standart developer shell";
        buildInputs = with pkgs; [
          python312
          python312Packages.pip
          poetry
        ];
        # shellHook = ''
        #   poetry install
        # '';
      };
    };
}
