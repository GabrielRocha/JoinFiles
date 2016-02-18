## Join Files

This script was built to join all directory files in only one file 


### Usage
**$ python join_files.py -h**
```
usage: join_files.py [-h] -p PATH [-f FILE]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Directory Path
  -f FILE, --file FILE  New file name
```

### Example
Files and content of /home/user/files_to_join path

**one.csv**
```
1;1;1;1;1
```

**two.csv**
```
2;2;2;2;2
```

##### Execute
**$ python join_files.py -p /home/user/files_to_join -f new.csv**

**$ cat new.csv**
```
1;1;1;1;1
2;2;2;2;2
```

##### Test
**$ python -m unittest discover**