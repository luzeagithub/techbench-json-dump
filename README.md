# techbench-json-dump
Dump Techbench metadata to a JSON file.

## Installation
```commandline
git clone https://github.com/luzeagithub/techbench-json-dump.git
cd techbench-json-dump
pip3 install -r requirements.txt
```

## Usage
```
usage: main.py [-h] [-o OUTPUT_FILE] start stop

Dump Techbench metadata to a JSON file.

positional arguments:
  start                 product edition ID to start with
  stop                  product edition ID to stop with

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        write JSON to file
```

## License
This project is licensed under the [MIT License](LICENSE).
