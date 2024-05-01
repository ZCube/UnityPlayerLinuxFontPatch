#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def patch_unityplayer_so(unityplayer_so_path):
    print(f"Patching {unityplayer_so_path}")
    with open(unityplayer_so_path, "rb") as f:
        data = f.read()
        data = data.replace(b"/run/host/fonts/", b"/usr/share/fonts")
    with open(unityplayer_so_path, "wb") as f:
        f.write(data)

def patch_unityplayer_so_recursive(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "UnityPlayer.so":
                patch_unityplayer_so(os.path.join(root, file))
def main():
    steamCommonPath = "~/.local/share/Steam/steamapps/common/"
    steamCommonPath = os.path.expanduser(steamCommonPath)
    patch_unityplayer_so_recursive(steamCommonPath)

if __name__ == "__main__":
    main()
