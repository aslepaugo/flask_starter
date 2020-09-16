API_KEY = ""

try:
    from settings_local import *
except ImportError:
    print("Import Error")