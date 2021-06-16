# Inspector
Inspector is a simple command line tool designed to understand how dictionary attacks on the FTP protocol work.

The script has different modes of use, you can test multiple targets at the same time and speed up the process by increasing the number of threads.

This project is made for educational purposes and is easy with it make tests on vulnerable virtual machines.

![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)
![Screenshot](https://img.shields.io/badge/License-GPL-red)
![Screenshot](https://img.shields.io/badge/Language-Python%203-blue)
![Screenshot](/Screenshots/Inspector.png)

## Installation

```bash
git clone https://github.com/intrackeable/Inspector.git
cd Inspector
pip install -r requirements.txt
python3 Inspector.py -h
```
## Example of usage

```python
python3 Inspector.py -F USER_PASS -T 5 -S 192.168.0.177
python3 Inspector.py -F USER_PASS -T 8 -S 192.168.0.181 192.168.0.182
```
