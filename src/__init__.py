import os
path = os.path.join(os.getcwd())
if path.endswith("src"):
    if "/" in path:
        path = "/".join(path.split("/")[:-1])
    else:
        path = "\\".join(path.split("\\")[:-1])
