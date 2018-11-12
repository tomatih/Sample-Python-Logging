# Sample Python Logging
This is an example of how to set up a two output logging in python.<br>
The two outputs are:
1. Info level colored output to stdout
2. Debug level output to a file
## Installation (And Setup)
1. Required libraries:
    - coloredlogs
2. Use `git clone https://github.com/tomatih/Sample-Python-Logging.git` to clone the repository
3. Copy the `logging.json` and `SetUp.py` files into your project directory
4. To use the Sample Logger add this at the top of the file
```python
import SetUp

logger = SetUp.GetLogger()
```
## Example
![Example Image](README%20Assets/Example.png)