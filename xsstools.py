#!/usr/bin/env python
#coding=utf-8
__author__ = 'Demon@ff0000.cc'

import sys

def xss2html(string):
    result = ''
    for i in string:
        result += '&#'+ str(ord(unicode(i, "utf-8"))) +';'
    return result

def xss2json(string):
    result = ''
    for i in string:
        j = hex(ord(unicode(i, "utf-8")))
        if len(j[2:]) == 1:
            result += '\\u000' + j[2:]
        elif len(j[2:]) == 2:
            result += '\\u00' + j[2:]
        elif len(j[2:]) == 3:
            result += '\\u0' + j[2:]
        else:
            result += '\\u' + j[2:]
    return result

def get_js_fromcharcode(string):
    code = []
    for i in string:
        code.append(str(ord(unicode(i, "utf-8"))))
    payload = ','.join(code)
    return 'String.fromCharCode('+ payload +')'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage is error! Please input your xss code. e.g: ./'+ sys.argv[0] + ' "<script>alert(1);</script>"'
    else:
        xss_code = sys.argv[1]
        print '[*] ====HTML Encode===='
        print xss2html(xss_code)
        print '[*] ====JSon Enconde===='
        print xss2json(xss_code)
        print '[*] ====JS fromCharCode Encode===='
        print get_js_fromcharcode(xss_code)
