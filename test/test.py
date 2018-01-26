# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
from configparser import ConfigParser
def run():
    pwd = os.path.split(os.path.realpath(__file__))[0]
    ppwd = os.path.split(pwd)[0]
    pppwd = os.path.join(ppwd, 'config.ini')
    awd = ConfigParser()
    awd.read(pppwd)
    print(awd.get('HOST', 'ip'))
if __name__ == '__main__':
    run()