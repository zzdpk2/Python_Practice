__author__ = "rex"
__date__ = "2020-10-04"

import re

s = "greedyaiiiiii"
# reg = "greedyai*"
# reg = "greedyai*?"
reg = re.compile("greedyai+?")
print(re.findall(reg, s))

s = "我的电话号码是: 010-89832343 0431-89847345  0432-7842342"
reg = re.compile("0\d{2}-\d{8}|0\d{3}-\d{8}|0\d{3}-\d{7,8}")
print(re.findall(reg, s))

s = "hellogreedyailove"
reg = re.compile("l{2}o(?=greedyai)")
print(re.findall(reg, s))
reg = "(?<=greedyai)[a-z]*"
print(re.findall(reg, s))
