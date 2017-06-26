# -*- coding: utf-8 -*-

# !/usr/bin/python
#
#  geo_redis.py
#
#
#  Created by vinhntb on 6/27/17.
#  Copyright (c) 2017 geo_redis. All rights reserved.

import connection


r = connection.connection_redis()

print r.set('foo', 'bar')
print r.get('foo')

