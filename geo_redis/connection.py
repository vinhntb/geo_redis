# -*- coding: utf-8 -*-

# !/usr/bin/python
#
#  connection.py
#
#
#  Created by vinhntb on 6/27/17.
#  Copyright (c) 2017 geo_redis. All rights reserved.

from redis.client import Redis


def connection_redis():
    conf = {
        'host': 'redisdb',
        'port': '6379',
        'db': 0
    }
    return Redis(**conf)
