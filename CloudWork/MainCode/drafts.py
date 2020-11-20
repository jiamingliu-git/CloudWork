import unittest
from CloudWork.MainCode.TestMethod import TestMethod_Box_01
import configparser
from ddt import ddt,data
from CloudWork.TestData.LoadFile_Method import LoadFile
from CloudWork.TestData.ConfigData import *
import requests


Alldata=LoadFile(TestCase_Path,0).get_data_auto()
# print(Alldata[5])

from CloudWork.TestData.ConfigData import *
import logging

# title = (Alldata[0]['CaseName'])
# def a():
#     '''{}'''
#     if {}:
#         c=a.replace('x',Alldata[0]['CaseName'])
#
#
# a='''aaaa'''
# print(a)
#
# '''{alldata['CaseName']}'''

import yaml
