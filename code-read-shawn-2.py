import csv
import argparse
import locale
import time
from datetime import datetime
from shutil import rmtree
from os import path, makedirs
import sys
import traceback

SERVICE_VERSION = '1.0.0'

def query_safe_my_code(s):
    return s.replace("'","''")