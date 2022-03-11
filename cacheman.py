"""
Utility library to ease managing picke-cache files
"""

import pickle
import sys
import os

CACHEMAN_NAME = ".cacheman"

class CacheMan(object):
    """
    Managing the cache to optimize performance
    """
    def __init__(self, project_name):
        """
        Arguments:
            @project_name [string]: the name of the project
        """
        if sys.platform == "win32":
            self.root_path = os.environ["APPDATA"]
        elif sys.platform == "linux":
            self.root_path = os.environ["HOME"]
        self.project_name = project_name

        self.folder_path = self.root_path
        self.folder_path = os.path.join(self.folder_path, CACHEMAN_NAME)
        self.folder_path = os.path.join(self.folder_path, self.project_name)
        os.makedirs(self.folder_path, exist_ok=True)
        return

    def Save(self, cache_name, cache_data):
        """
        Save the cache data to the file with the given name

        Arguments:
            @cache_name [string]: the name of the cache file
            @cache_data [any]: the data to be saved by pickling
        """
        cache_path = os.path.join(self.folder_path, cache_name)
        with open(cache_path, "wb") as f:
            pickle.dump(cache_data, f)
        return
    
    def Load(self, cache_name, default_value=None):
        """
        Load the cache data from the file with the given name

        Arguments:
            @cache_name [string]: the name of the cache file
        """
        cache_path = os.path.join(self.folder_path, cache_name)
        try:
            with open(cache_path, "rb") as f:
                cache_data = pickle.load(f)
        except:
            return default_value
        return cache_data


if __name__ == "__main__":
    a = {
        "aa": 1,
        "bb": 3
    }
    print(a)

    cacheman = CacheMan("test")
    cacheman.Save("testcache", a)
    b = cacheman.Load("testcache")
    print(b)