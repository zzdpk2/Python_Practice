__author__ = "Rex Zhu"
__date__ = "2020-10-02 22:15"

import aiml
k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("load aiml b")

while True:
    print(k.respond(input("input >> ")))
