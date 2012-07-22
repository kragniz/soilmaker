#!/usr/bin/env python
import os
for i in range(84):
    os.system('touch profile%s/profile%s' % (i+1, i+1))

