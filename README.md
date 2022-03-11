# CacheMan
## Description
A library for managing python pickled object cache.

## Usage
```python
from cacheman import CacheMan
a = {
    "aa": 1,
    "bb": 3
}
print(a)

cacheman = CacheMan("test")
cacheman.Save("testcache", a)
b = cacheman.Load("testcache")
print(b)
```
Caches will store at following pathes:
- Windows
  - `%APPDATA%/.cacheman/[PROJECT_NAME]/[CACHE_NAME]`
- Linux
  - `%USER_HOME%/.cacheman/[PROJECT_NAME]/[CACHE_NAME]`

## Tested environment
`Windows 10 x64 + Python 3.9`