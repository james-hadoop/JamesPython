import datetime
import re
import datetime
import sys

import configobj
import pymysql
import json
import os
import re
import base64

import sqlparse


def main():
    # -*- coding: utf-8 -*-

    import re

    txt = "--  纯     图     文TOK_BACKSLASH_N"
    txt = "hello world --  纯     图     文TOK_BACKSLASH_N world hello   --  纯   图     文TOK_BACKSLASH_N"

    print(re.sub(r'\-\-\s*%s\s*TOK_BACKSLASH_N', txt, 'TOK_BACKSLASH_N'))


if __name__ == '__main__':
    main()
