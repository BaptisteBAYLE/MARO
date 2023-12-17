import time
from icecream import ic
import sys
sys.path.append('src')
from flowshop import Flowshop


a = 20
ic(int(a/5 * 4) + int((a+1)/5))