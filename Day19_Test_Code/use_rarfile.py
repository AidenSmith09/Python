# /bin/etc/env Python
# -*- coding: utf-8 -*-
import rarfile
file = rarfile.RarFile('./test_pass.rar')
file.extractall('./',pwd='13110001234')