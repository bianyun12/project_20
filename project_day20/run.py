import os,sys
from unittestreport import TestRunner
import unittest
from handle_func.handle_path import REPORT_DIR,CASE_DIR,CONF_DIR
from handle_func.handle_config import config,conf
dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages")
suite=unittest.defaultTestLoader.discover(CASE_DIR)
runner=TestRunner(suite,
                 filename=conf.get('report','report_name'),
                 report_dir=REPORT_DIR,
                 title=conf.get('report','title'),
                 tester=conf.get('report','taster'),
                 desc=conf.get('report','desc'),
                 templates=1)
runner.run()