1. Copy repo to another temporary location
2. Delete `./yamljson2xml.egg-info`, `./src/yamljson2xml.egg-info`, and `./src/__pycache__`
3. Run `pyinstaller --onefile --paths="./src" "src/yamljson2xml.py"` from root directory.
4. extract the `.exe` file from the `./dist` folder.