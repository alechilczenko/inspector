# Inspector
Inspector is a simple command line tool for performing dictionary attacks in FTP servers.

At the moment this tool, only work with a custom [USER:PASSWORD] wordlist. If you don't have one, dont't worry, you can generate it with WORDLISTGEN script.

![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)
![Screenshot](https://img.shields.io/badge/License-GPL-red)
![Screenshot](https://img.shields.io/badge/Language-Python%203-blue)
![Screenshot](/Screenshots/screen1.png)

## Installation

```bash
git clone https://github.com/intrackeable/FTP-Inspector.git
cd FTP-Inspector
pip install -r requirements.txt
python3 FTP-Inspector.py -h
```
![Screenshot](/Screenshots/screen2.png)
## Example of usage

```python
python3 FTP-Inspector.py -F USER_PASS -T 5 -S 192.169.0.177
```
## Features
- [x] Select number of threads.
- [ ] Anonymizing login attempts using TOR network.
- [ ] Attack multiple servers simultaneously.
## Attention
This project was created for educational purposes and should not be used in environments without legal authorization.
