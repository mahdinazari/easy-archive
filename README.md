# easy-archive - An archive reader tool for python


### Supported format
- .rar
- .zip
- .tar, '.tar.bz2', '.tar.gz', 'tar.xz', '.tgz', '.tz2'
- .7z
- ...


### Installation 

```python
$ pip install easy_archive
```

### Usage

```python
from easy_archive import Archive

archive = Archive('archive_file_path')
archive.[namelist | list | is_encrypted | close]

archive.[extract | extractall]('destination_path')
```

### Features
- *namelist:* Returns list of filenames in archive.
- *list:* Returns pretty list of filenames in archive. 
- *is_encrypted:* Specified the archive require password for extract or not.
- *extract:* Extract single archive level in current path or given path
    directory.
- *extractall:* Extract all archived level in given path directory.
- *close:* Close open archive file.


### development
For development execute following:

```python
pip install -r requirement-dev.txt
pip install -e 
```

