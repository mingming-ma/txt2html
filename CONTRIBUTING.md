## How to Install 

**In command line:**

Make sure python3 is installed:
```bash
python3 --version
```
Make sure tomli is downloaded:
```bash
pip3 install tomli
```

Clone the Repo

```bash
git clone https://github.com/mingming-ma/txt2html.git
cd txt2html 
```

Make the tool executable
```bash
chmod +x txt2html.py
```

## Formatter

1. VS Code extension
If you are using VS Code and havn't already installed [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter), Black Formatter extension can do for you. You can enable format on save for python by having the following values in your settings
```json
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
      }
}
```

1. Install Black from command line
You can also install by running the following command:
```bash
pip3 install black
```
2. Run Black on the Code
```bash
black txt2html.py
```

## Linter

1. VS Code extension
If you are using VS Code and havn't already installed [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8), Flake8 extension for Visual Studio Code will be automatically executed when you open a Python file.
2. Put the Configure Flake8 file at the project directory 
`.flake8` file:
```
[flake8]
max-line-length = 88
extend-ignore = E203, E704
```

1. Install Flake8 from command line
You can also install from command line by running the following command:
```bash
pip3 install flake8
```
2. Put the Configure Flake8 file at the project directory 
`.flake8` file:
```
[flake8]
max-line-length = 88
extend-ignore = E203, E704
```
3. Run Flake8 on the Code
```bash
flake8 txt2html.py
```