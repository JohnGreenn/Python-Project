# _*_coding:utf-8_*_
# creat by John Green

import os
import sys
from db import __init__


PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(PATH)
sys.path.append(PATH)

