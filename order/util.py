# source weixin.py
from __future__ import unicode_literals
import hashlib
import time
import random
try:
    from lxml import etree
except ImportError:
    from xml.etree import cElementTree as etree
except ImportError:
    from xml.etree import ElementTree as etree

FAIL = "FAIL"
SUCCESS = "SUCCESS"

#generate out_trade_no and product_id
def gen_trade_no():
    return str(int(time.time()))+str(random.randrange(100,999))

def sign(raw,mch_key):
    raw = [(k, str(raw[k]) if isinstance(raw[k], int) else raw[k])
           for k in sorted(raw.keys())]
    s = "&".join("=".join(kv) for kv in raw if kv[1])
    s += "&key={0}".format(mch_key)
    return hashlib.md5(s.encode("utf-8")).hexdigest().upper()

def to_xml(raw):
    s = ""
    for k, v in raw.items():
        s += "<{0}>{1}</{0}>".format(k, v)
    s = "<xml>{0}</xml>".format(s)
    return s.encode("utf-8")

def to_dict(content):
    raw = {}
    root = etree.fromstring(content)
    for child in root:
        raw[child.tag] = child.text
    return raw

def reply(msg, ok=True):
    code = SUCCESS if ok else FAIL
    return to_xml(dict(return_code=code, return_msg=msg))