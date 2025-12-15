# autonumba 🚀

Autonumba is an aggressive auto-JIT tool that scans Python code and injects `@njit` wherever it safely can, with optional ahead-of-time (AOT) compilation into native binaries.

## Features ✨

* ⚡ Automatic JIT and AOT compilation for instant native speed
* 📂 Boost folders, single files, or installed libraries
* 🏷️ `@libname` syntax for installed site-packages
* ❌ `exclude.txt` support for skipping files
* ⚙️ Configurable Numba flags for cache, fastmath, parallel, nogil, boundscheck
* 🖥️ CLI-first, fast, clean workflow

## Installation 💻

```bash
pip install autonumba
```

or from source:

```bash
git clone https://github.com/pro-grammer-SD/autonumba.git
cd autonumba
python -m pip install --user .
```

or use the prebuilt binary in bin/ `(bin/autonumba.exe)`

## Usage 📝

Boost a folder:

```bash
python -m autonumba src -c -f -p -n -b
```

Boost a single file:

```bash
python -m autonumba main.py -c -f
```

Boost an installed library:

```bash
python -m autonumba @mylib -c -f -p
```

Modify files in-place:

```bash
python -m autonumba src -i -c -f -p -n -b
```

Enable ahead-of-time compilation:

```bash
python -m autonumba src --aot
```

Disable Rich output (for Windows encoding issues):

```bash
python -m autonumba src -nr
```

Nuitka compile to EXE after boost:

```bash
python -m autonumba main.py -cm
```

## CLI Flags 🏷️

| Flag              | Description                                      |
| ----------------- | ------------------------------------------------ |
| -i, --inplace     | ✏️ Modify files in place                         |
| -c, --cache       | 💾 Enable njit cache                             |
| -f, --fastmath    | ⚡ Enable fastmath                                |
| -p, --parallel    | 🔀 Enable parallel loops                         |
| -n, --nogil       | 🛠 Release GIL                                   |
| -b, --boundscheck | 📏 Enable bounds checking                        |
| --aot             | 🚀 Force ahead-of-time compilation into binaries |
| -cm, --compile    | 🖥 Nuitka compile to EXE after boost             |
| -nr, --no-rich    | ❌ Disable rich output / emojis                   |

Flags are **enabled by default**. Pass flags to selectively override defaults.

## Notes ⚠️

* Designed for numeric-heavy code.
* Dynamic Python features (strings, IO, objects) may not compile correctly.
* Use responsibly. Native binaries are fast but can break dynamic behavior.

## GitHub Stats 📊

![GitHub Repo Stats](https://github-readme-stats-fast.vercel.app/api/pin/?username=pro-grammer-SD\&repo=autonumba\&theme=radical)
![GitHub Stats](https://github-readme-stats-fast.vercel.app/api?username=pro-grammer-SD\&show_icons=true\&theme=radical)

## Badges 🎉

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build Status]([https://img.shields.io/badge/build-pass](https://img.shields.io/badge/build-pass)
