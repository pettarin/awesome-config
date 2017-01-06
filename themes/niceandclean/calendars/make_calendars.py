#!/usr/bin/env python
# coding=utf-8

import calendar
import datetime
import io
import sys


__author__ = "Alberto Pettarin"
__email__ = "alberto@albertopettarin.it"
__copyright__ = "Copyright 2015-2017, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__status__ = "Production"
__version__ = "1.1.8"


def usage():
    """ Print usage message """
    print("")
    print("Usage:")
    print("  $ python %s [YYYY MM]" % sys.argv[0])
    print("")


def increment(year, month, inc):
    """ Increment the month and, if needed, the year """
    month += inc
    while month > 12:
        year += 1
        month -= 12
    return (year, month)


def save_month_file(year, month, inc):
    """ Save month to file """
    p_year, p_month = increment(year, month, inc)
    s = calendar.month(p_year, p_month)
    lines = [l for l in s.split(u"\n") if len(l.strip()) > 0]
    # right-justify month name (first line)
    lines[0] = lines[0].strip().rjust(20)
    file_name = "month%d" % (inc + 1)
    with io.open(file_name, "w", encoding="utf-8") as f:
        f.write(u"\n".join(lines))
    print(u"[INFO] Created file %s for %d %d" % (file_name, p_year, p_month))


def main():
    if ("-h" in sys.argv) or ("--help" in sys.argv):
        usage()
        sys.exit(2)
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
            month = int(sys.argv[2])
            if (month < 1) or (month > 12):
                raise ValueError
        except:
            print(u"")
            print(u"[ERRO] Invalid value for year or month, using current date instead")
            print(u"")

    for i in range(3):
        save_month_file(year, month, i)


if __name__ == "__main__":
    main()
