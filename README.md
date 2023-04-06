# File-Shield

File-Shield is a command-line file locking application written in Python. It allows you to monitor changes in the file system and lock any new files created by converting them into base64 data. You can also unlock previously locked files by converting the base64 data back to the original file contents.

## Installation

To install File-Shield, you will need to have [Python 3](https://www.python.org/downloads/) installed on your computer. Once you have Python 3 installed, you can download the `shield.py` file from this repository and place it in a directory of your choice.

## Usage

To use File-Shield, open a terminal or command prompt and navigate to the directory where `shield.py` is located. Then, run the following command:

```bash
python shield.py --lock/--unlock --file /path/to/file
```
Replace /path/to/file with the actual path to the file you want to lock or unlock.

The ***--lock*** or ***-l*** parameter is used to lock the file, which means that the file data will be converted into base64. The ***--unlock*** or ***-ulk*** parameter is used to unlock the file, which means that the base64 data will be converted back to the original file contents.

Here's an example of how to lock a file:
```bash
python shield.py --lock --file /path/to/file.txt
```
And here's an example of how to unlock a file:
```bash
python shield.py --unlock --file /path/to/file.txt
```

## Contributing

Contributions to File-Shield are welcome! If you find a bug or have a feature request, please [open an issue](https://github.com/VishalShenoy2002/File-Shield/issues). If you would like to contribute code, please fork the repository and submit a pull request.

## License

File-Shield is licensed under the MIT License. See LICENSE for more information.
