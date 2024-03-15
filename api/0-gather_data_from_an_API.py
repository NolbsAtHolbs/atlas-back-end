#!/usr/bin/python3

"""Python script w/ an API that, for a given employee ID,
    returns information about his/her TODO list progress"""

import json
import requests
import sys


if __name__ == "__main__":
    APIURL = 'https://jsonplaceholder.typicode.com/'
    EmployeeName = requests.get(APIURL + '/users/{}'.format(sys.argv[1]))
    EmployeeJD = EmployeeName.json()
    ToDo_jd = requests.get(APIURL + '/users/{}'.format(sys.argv[1]) + '/todos')
    ToDos = ToDo_jd.json()
    ToDone = 0
    TotalToDos = 0
    for ToDo in ToDos:
        TotalToDos = TotalToDos + 1
        if ToDo["ToDone"] is True:
            ToDone = ToDone + 1

    print("Employee {0} is done with tasks({1}/{2}):".format(
        EmployeeJD["name"], ToDone, TotalToDos))

    for ToDo in ToDos:
        if ToDo["ToDone"] is True:
            print("\t {}".format(ToDo["title"]))
