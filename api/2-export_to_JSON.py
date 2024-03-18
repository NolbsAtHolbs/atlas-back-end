#!/usr/bin/python3

"""Exports data to JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    APIURL = "https://jsonplaceholder.typicode.com/"
    FileName = "{}.json".format(sys.argv[1])
    EmployeeName = requests.get(APIURL + '/users/{}'.format(sys.argv[1]))
    EmployeeJD = EmployeeName.json()
    ToDos = requests.get(APIURL + "/users/{}".format(sys.argv[1]) + "/todos")
    ToDosJD = ToDos.json()
    EmployeeJDID = "{}".format(EmployeeJD["id"])
    EmployeeJDUpdate = {EmployeeJDID: []}
    for ToDo in ToDosJD:
        TasksData = {"task": ToDo["title"],
                     "completed": ToDo["completed"],
                     "username": EmployeeJD["name"]}
    EmployeeJDUpdate[EmployeeJDID].append(TasksData)
    with open(FileName, "w") as file:
        file.write(json.dump(EmployeeJDUpdate))
