__author__ = "rex"
__date__ = "2020-09-23"

# Regular expression

import re

# s = "牛逼公司http://www.baidu.com"
# reg = "http://[w3]{3}\.[a-Z0-9]*\.com"
# result = re.findall(reg, s)
#
# print(result)

# s = "hello world"
# reg = "hello"
# print(re.findall(reg, s))

# s = "fsad_as_das是范德萨@~#&范德萨  sfs_d   f1_232 "
# print(re.findall("\w", s))
# print(re.findall("\d", s))
# print(re.findall("\s", s))
# print(re.findall("^f", s))

# django url匹配使用正则

s = "hhhsda1312....说的很对4575643是开发环境dsfsdf....sas154534s"
print(re.findall("\d{3}", s))
print(re.findall("[\da-z]+", s))

