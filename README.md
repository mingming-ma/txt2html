<h1 align="center">txt2html</h1>

<div align="center">
 
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## Features

- This is a command-line tool process input txt files output html files.

### Planned features
- [ ] User specified output path
- [ ] Set title from input file content
- [ ] Additional \<br \/\> tags to match empty lines


## How to Install 

**In command line:**

Make sure python3 is installed:
```bash
python3 --version
```

Clone the Repo

```bash
git clone https://github.com/mingming-ma/txt2html.git
$ cd txt2html 
```

Make the tool executable
```bash
chmod +x txt2html.py
```
## Usage

To generate html from a txt file: 
```bash
./txt2html.py input_file.txt
```
To generate html from a folder which has txt files: 
```bash
./txt2html.py folder-name
```

# Command Flags

<!-- Available command options:
```
-v,--version - Displays the version of the tool
-h,--help - Displays the help message
``` -->

| Command   | Description |
| --------- | ----------- |
| -v, --version | Displays the version of the tool |
| -h, --help | Displays the help message |