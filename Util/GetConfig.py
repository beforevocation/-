# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
from configparser import ConfigParser

class GetConfig(object):

    def __init__(self):
        self.pwd = os.path.split(os.path.realpath(__file__))[0]
        self.config_path = os.path.join(os.path.split(self.pwd)[0], 'config.ini')
        self.config_parse = ConfigParser()
        self.config_parse.read(self.config_path)

if __name__ == '__main__':
    #测试读取配置文件
    getConfig = GetConfig()
    print(getConfig.config_parse.get('HOST', 'ip'))