__author__ = "rex"
__date__ = "2020-10-04"

import re

s = "greedyaiiiiii"
# reg = "greedyai*"
# reg = "greedyai*?"
reg = "greedyai+?"
print(re.findall(reg, s))

