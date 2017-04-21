#!/usr/bin/env python3

import pprint

def coalesce(*args):
    return next(s for s in args if s is not None)

def coalesce_test(*args):
    print( '%s -> %s' % (pprint.pformat(args),coalesce(*args)) )

if __name__ == '__main__':
    coalesce_test(1,2,3)
    coalesce_test(None,1,2,3)
    coalesce_test('a','b','c')
    coalesce_test(None,'a','b','c')
