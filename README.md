# DLCheck
Downloads a file and checks it against a checksum

## Prerequesites
- Python 3.5

## Installation

## Examples
```
import dlcheck
# Download without checking
dlcheck("[URL]") 

# Download and store the output in a folder
dlcheck("[URL]", output_directory_path=[FOLDER]) 

# Download with checksum check
dlcheck("[URL]", check_method="[md5|sha1|sha256|...]", hash_digest="[HASH]") 

# Download and gives the current downloaded and the file size to an external function while downloading.
dlcheck("[URL]", ..., observer=[OBSERVER_FUNCTION]) 
```

## To Do
To do: write the To Do section
