#!/usr/bin/env python
# coding: utf-8

import socket
import sqlite3
import struct
import sys
import json

def ip2uint32(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]


class ReservedIPs:
    """List of reserved IPs.
    http://en.wikipedia.org/wiki/Reserved_IP_addresses
    """
    IPs = [
        # network                       netmask
        (ip2uint32("0.0.0.0"),          ip2uint32("255.0.0.0")),
        (ip2uint32("10.0.0.0"),         ip2uint32("255.0.0.0")),
        (ip2uint32("100.64.0.0"),       ip2uint32("255.192.0.0")),
        (ip2uint32("127.0.0.0"),        ip2uint32("255.0.0.0")),
        (ip2uint32("169.254.0.0"),      ip2uint32("255.255.0.0")),
        (ip2uint32("172.16.0.0"),       ip2uint32("255.240.0.0")),
        (ip2uint32("192.0.0.0"),        ip2uint32("255.255.255.248")),
        (ip2uint32("192.0.2.0"),        ip2uint32("255.255.255.0")),
        (ip2uint32("192.88.99.0"),      ip2uint32("255.255.255.0")),
        (ip2uint32("192.168.0.0"),      ip2uint32("255.255.0.0")),
        (ip2uint32("192.18.0.0"),       ip2uint32("255.254.0.0")),
        (ip2uint32("198.51.100.0"),     ip2uint32("255.255.255.0")),
        (ip2uint32("203.0.113.0"),      ip2uint32("255.255.255.0")),
        (ip2uint32("224.0.0.0"),        ip2uint32("240.0.0.0")),
        (ip2uint32("240.0.0.0"),        ip2uint32("240.0.0.0")),
        (ip2uint32("255.255.255.255"),  ip2uint32("255.255.255.255")),
    ]

    @classmethod
    def test(cls, ip):
        for (network, netmask) in cls.IPs:
            if ip & netmask == network:
                return True
        return False


def search_geoip(ip):
    try:
        ip = ip2uint32(socket.gethostbyname(ip))
    except Exception, e:
        print e
        return

    if ReservedIPs.test(ip) is True:
        return "RD,Reserved,,,,,,,,"

    conn = sqlite3.connect("ipdb.sqlite")
    curs = conn.cursor()

    curs.execute(
        "SELECT "
        "  city_location.country_code, country_blocks.country_name, "
        "  city_location.region_code, region_names.region_name, "
        "  city_location.city_name, city_location.postal_code, "
        "  city_location.latitude, city_location.longitude, "
        "  city_location.metro_code, city_location.area_code "
        "FROM city_Blocks "
        "  NATURAL JOIN city_location "
        "  INNER JOIN country_blocks ON "
        "    city_location.country_code = country_blocks.country_code "
        "  INNER JOIN region_names ON "
        "    city_location.country_code = region_names.country_code AND "
        "    city_location.region_code = region_names.region_code "
        "WHERE city_blocks.ip_start < ? "
        "ORDER BY city_blocks.ip_start DESC LIMIT 1", (ip,))

    rs = curs.fetchone() or []
    curs.close()
    conn.close()
    return ",".join(map(lambda s: unicode(s).encode("utf-8"), rs))


if __name__ == "__main__":
    try:
        ip = sys.argv[1]
    except IndexError:
        print "usage: search ip"
        sys.exit(1)

    print search(ip)
