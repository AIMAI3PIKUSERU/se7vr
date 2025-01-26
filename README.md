
# se7vr
[简体中文](https://github.com/AIMAI3PIKUSERU/se7vr/blob/master/README_cn.md)
#### Introduction
This is a lightweight, highly customizable server program built with Python.

#### Additional Libraries
This program is built on the **Flask** library. To install it, run:

```shell
pip install flask
```

#### Usage Instructions

Run the program by typing `python main.py` in the terminal. Then, open your browser and go to [127.0.0.1:8000](http://127.0.0.1:8000) to access the server.  
All files in the repository, except `main.py`, are optional and only provide additional customization options.  
If you want to simulate the interface of `python -m http.server`, run `python main.py -s`.  
Use the `--help` or `-h` parameter to see available options. The output is as follows:

| Option      | Description |
|-------------|-------------|
| --bind/-b   | [ip=0.0.0.0]: The specific IP address to bind to. |
| --dir/-d    | [directory=.]: The directory to serve files from. |
| --active/-a | Actively reload "template.html," "404.html," and "filter.py" on each request. |
| --encode/-e | Encode the path (use this when characters are displayed incorrectly). |
| --nocache/-n| Add the "Cache-Control: no-cache" HTTP header to each response. |
| --single/-s | Serve a dynamically generated page. |

## About the --single/-s Flag and Customization

When this flag is not enabled, each directory access will return `template.html` (located in the same directory as `main.py`) as the response body to the client. Additionally, certain placeholders in `template.html` will be dynamically replaced based on the current directory. The placeholders and their meanings are as follows:

| Placeholder     | Description |
|-----------------|-------------|
| `${#CD}`        | The `href` attribute of an `<a>` tag pointing to the parent directory. |
| `${#FULLPATH}`  | The full path of the current directory. |
| `${#PATH}`      | The relative path of the running directory. |
| `${#LIST_NAME}` | Names of all files and subdirectories in the current directory (one per line). |
| `${#LIST_TYPE}` | Indicates whether each entry is a file or a directory, using `0` for files and `1` for directories (one per line). Matches the order of `${#LIST_NAME}`. |
| `${#LIST_LEN}`  | The number of entries in `${#LIST_NAME}` and `${#LIST_TYPE}`. |

If a requested file is not found, the server will return `404.html`.

---

#### About filter.py

The `filter.py` file should define a function named `fileFilter` with the following structure:

```python
def fileFilter(fullpath, name, isdir):
    if isdir:
        return 1  # If it is a directory, return 1 (True), allowing all directories.
    if 'secret' in name:
        return 0  # If the filename contains 'secret', return 0 (False), blocking this file.
    return 1
```

This function is used to filter files and directories based on specific criteria.
