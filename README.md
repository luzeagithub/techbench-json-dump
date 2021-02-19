# techbench-json-dump
Dump Tech Bench metadata to a JSON file.

The latest generated dump can be found [here](https://techbench.luzea.ovh/dump.json).

## Installation
```
git clone https://github.com/luzeagithub/techbench-json-dump.git
cd techbench-json-dump
pip3 install -r requirements.txt
```

## Usage
```
usage: main.py [-h] [--json-indent JSON_INDENT] [--threads THREADS] start stop output-file

Dump Tech Bench metadata to a JSON file.

positional arguments:
  start                 product edition ID to start with
  stop                  product edition ID to stop with
  output-file           write JSON to file (merge if already exists)

optional arguments:
  -h, --help            show this help message and exit
  --json-indent JSON_INDENT
                        how many spaces an indentation in the final JSON file is (default: 0, no indentation)
  --threads THREADS     number of threads used (default: 64)
(venv) luca@lucas-pc:~/PycharmProjects/techbench-json-dump$ ./main.py -h
usage: main.py [-h] [--json-indent JSON_INDENT] [--threads THREADS] start stop output-file

Dump Tech Bench metadata to a JSON file.

positional arguments:
  start                 product edition ID to start with
  stop                  product edition ID to stop with
  output-file           write JSON to file (merge if already exists)

optional arguments:
  -h, --help            show this help message and exit
  --json-indent JSON_INDENT
                        spaces for JSON indentation (default: 0)
  --threads THREADS     number of threads used (default: 64)
```

## Contributing
Yes, please. Fork this repository and start working. After you are done with it, submit a pull request and I will review your changes.

## License
This project is licensed under the [MIT License](LICENSE).
