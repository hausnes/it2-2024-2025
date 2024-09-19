{
  description = "Samleside for IT2, 2024-2025, Python.";

  # Package repository
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { nixpkgs, ... }@inputs:
    let
      # Funksjoner for å gjøre ting enklere
      lib = nixpkgs.lib;
      systems = lib.systems.flakeExposed;
      pkgsFor = lib.genAttrs systems (system: import nixpkgs { inherit system; });
      forEachSystem = f: lib.genAttrs systems (system: f pkgsFor.${system});
    in
    {
      devShells = forEachSystem (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            # Verktøy for nix
            nixfmt-rfc-style
            nixd
            # Verktøy for python
            (python312.withPackages (
              ps: with ps; [
                numpy
                matplotlib
              ]
            ))
            black
            pyright
            # Flytskjemaer
            plantuml
          ];
        };
      });

    };
}
