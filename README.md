## Prefabs2Blueprints
Working as of Space Engineers version: 1.208

A Python script that converts Space Engineers Prefab files to Blueprints.

### Requirements
- [Download and install Python][0] (only tested with 3.x, 2.x is unknown)
- [Download the scripts][1]

### Setup
1. Copy `config.py` and `convert.py` files into the same folder.
2. Open `config.py` with a text editor to check or change the default values.
   - The default values should match with a default Space Engineers install.
   - If you have a non-default install, change and save the paths accordingly.
3. Run (double-click) the `convert.py` file.

### Notes
The script should make new folders for each new blueprint automatically.

The original project had notes that past version game settings were not retained in the created blueprints. I'm not sure of what settings might be missing, but this fork works for me.

Please report any issues using the [GitHub issue tracker][2].

[0]: https://www.python.org/downloads/
[1]: https://github.com/Klexur/Prefabs2Blueprints/archive/master.zip
[2]: https://github.com/Klexur/Prefabs2Blueprints/issues
