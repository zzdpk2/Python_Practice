__author__ = "rex"
__date__ = "2020-10-06"

import aiml

k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("load aiml b")
while True:
    # print(k.respond(input("Please enter>>")))
    question = input("Please enter>>")
    answer = k.respond(question)
    answer_1 = answer.replace(" ", "")
    print(answer_1)
