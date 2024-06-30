{
  description = "Testing";

  inputs = {
    nixpkgs.url      = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url  = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        overlays = [];
        pkgs = import nixpkgs {
          inherit system overlays;
        };

        package = pkgs.python3Packages.buildPythonApplication rec {
          pname = "mopidy-dwebble";
          version = "0.1.0";

          src = ./.;
          propagatedBuildInputs = [ pkgs.mopidy ];

          doCheck = false;
          pythonImportsCheck = [ "mopidy_dwebble" ];
        };
      in
      {
        packages.default = package;

        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            (python3.withPackages (pp: [
            ]))
            mopidy
            mopidy-mpd
          ];
        }; 
      }
    );
}
