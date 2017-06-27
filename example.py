# -*- coding: utf-8 -*-

# !/usr/bin/python
#
#  example.py
#
#
#  Created by vinhntb on 6/27/17.
#  Copyright (c) 2017 geo_redis. All rights reserved.

import sys
from bunch import Bunch
from constants import GEO_USER_VISITED
from geo_redis.geo_redis import GeoRedis


def add_user_visited():
    user_1 = Bunch(longitude=13.583333, latitude=37.316667, member='101')  # The member is user_id
    user_2 = Bunch(longitude=13.361389, latitude=38.115556, member='102')  # The member is user_id
    user_3 = Bunch(longitude=13.583433, latitude=37.317667, member='103')  # The member is user_id
    user_4 = Bunch(longitude=13.583533, latitude=37.318667, member='104')  # The member is user_id
    user_5 = Bunch(longitude=13.583633, latitude=37.318767, member='105')  # The member is user_id
    user_6 = Bunch(longitude=13.583733, latitude=37.318867, member='106')  # The member is user_id
    user_7 = Bunch(longitude=13.361389, latitude=38.115556, member='107')  # The member is user_id
    user_8 = Bunch(longitude=15.087269, latitude=37.502669, member='108')  # The member is user_id

    redis_instance = GeoRedis()
    redis_instance.geo_add(GEO_USER_VISITED, **user_1)
    redis_instance.geo_add(GEO_USER_VISITED, **user_2)
    redis_instance.geo_add(GEO_USER_VISITED, **user_3)
    redis_instance.geo_add(GEO_USER_VISITED, **user_4)
    redis_instance.geo_add(GEO_USER_VISITED, **user_5)
    redis_instance.geo_add(GEO_USER_VISITED, **user_6)
    redis_instance.geo_add(GEO_USER_VISITED, **user_7)
    redis_instance.geo_add(GEO_USER_VISITED, **user_8)


def get_geo_radius():
    redis_instance = GeoRedis()
    unit = 'm'
    results = redis_instance.geo_radius(name=GEO_USER_VISITED, longitude=13.58, latitude=37.316, radius=500, unit=unit,
                                       withcoord=True, withdist=True)

    """The results are in nested array depend of parameters input. At this example, we have parameters:
        withcoord, withdist, withash. So result
        1) member (user_id)     [0]
        2) distance             [1]
        3)  1) longitude        [2][0]
            2) latitude         [2][1]
    """

    print "The results: \n"
    print "Total: %s" % len(results)
    for member in results:
        print '--------------------------------------\n'
        print "member: %s \n" % member[0]
        print "distance: %s%s \n" % (member[1], unit)
        print "longitude: %s \n" % member[2][0]
        print "latitude: %s \n" % member[2][0]


def main(argv):
    add_user_visited()
    get_geo_radius()


if __name__ == '__main__':
    main(sys.argv)




