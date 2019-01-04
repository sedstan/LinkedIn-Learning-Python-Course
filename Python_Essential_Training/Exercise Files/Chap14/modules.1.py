#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import datetime

def main():
    now = datetime.datetime.now()
    print(now.year, now.day, now.month, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__': main()
