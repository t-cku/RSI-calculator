{ pkgs }: {
  deps = [
    pkgs.cairo
    pkgs.ffmpeg-full
    pkgs.freetype
    pkgs.ghostscript
    pkgs.glibcLocales
    pkgs.gobject-introspection
    pkgs.gtk3
    pkgs.pkg-config
    pkgs.qhull
    pkgs.tcl
    pkgs.tk
    pkgs.stdenv.cc.cc.lib
    pkgs.gcc-unwrapped.lib
  ];
}