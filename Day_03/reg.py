__author__ = "rex"
__date__ = "2020-10-04"

import re

s = "greedyaiiiiii"
# reg = "greedyai*"
# reg = "greedyai*?"
reg = "greedyai+?"
print(re.findall(reg, s))

s = "我的电话号码是: 010-89832343 0431-89847345  0432-7842342"
reg = "0\d{2}-\d{8}|0\d{3}-\d{8}|0\d{3}-\d{7,8}"
print(re.findall(reg, s))
