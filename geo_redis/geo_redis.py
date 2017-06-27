# -*- coding: utf-8 -*-

# !/usr/bin/python
#
#  geo_redis.py
#
#
#  Created by vinhntb on 6/27/17.
#  Copyright (c) 2017 geo_redis. All rights reserved.

from bunch import Bunch
from connection import connection_redis


class GeoRedis(object):

    def __init__(self):
        self.redis = connection_redis()

    def geo_add(self, name, longitude, latitude, member):
        return self.redis.geoadd(name, longitude, latitude, member)

    def geo_radius(self,name, longitude, latitude, radius, unit=None, withdist=False, withcoord=False, withhash=False,
                   count=None, sort=None, store=None, store_dist=None):

        values = Bunch(name=name, longitude=longitude, latitude=latitude, radius=radius, unit=unit, withdist=withdist,
                       withcoord=withcoord, withhash=withhash, count=count, sort=sort, store=store, store_dist=store_dist)
        return self.redis.georadius(**values)

    def geo_radius_by_member(self, name, member, radius, unit=None, withdist=False, withcoord=False, withhash=False,
                             count=None, sort=None, store=None, store_dist=None):

        values = Bunch(name=name, member=member, radius=radius, unit=unit, withdist=withdist, withcoord=withcoord,
                       withhash=withhash, count=count, sort=sort, store=store, store_dist=store_dist)
        return self.redis.georadiusbymember(**values)






