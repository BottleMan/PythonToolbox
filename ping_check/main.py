#!/usr/bin/env python
# coding: utf-8

from tcping import Ping


def ping_check():
    ping = Ping('192.168.0.116', 80, 60)
    ping.ping(10)

    ret = ping.result.rows
    for r in ret:
        print(r)

    ret = ping.result.raw
    print(ret)

    ret = ping.result.table
    print(ret)


if __name__ == '__main__':
    ping_check()
