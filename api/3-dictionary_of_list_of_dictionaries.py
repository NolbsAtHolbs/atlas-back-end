#!/usr/bin/python3

"""Exports dictionary data to JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    APIURL = "https://jsonplaceholder.typicode.com/"
    EmployeeDoD = {}
    EmployeeName = requests.get(APIURL + "/users/{}".format(sys.argv[1]))
    EmployeeJD = EmployeeName.json()
    for Employee in EmployeeJD:
        EmployeeJDID = "{}".format(Employee["id"])
        EmployeeJDUpdate = {EmployeeJDID: []}
        ToDos = requests.get(APIURL + EmployeeJDID)
        ToDosJD = ToDos.json()
        for ToDo in ToDosJD:
            TasksData = {"username": EmployeeJD["username"],
                         "task": ToDo["title"],
                         "completed": ToDo["completed"]}
            EmployeeJDUpdate[EmployeeJDID].append(TasksData)
        EmployeeDoD.update(EmployeeJDUpdate)
    with open('todo_all_employees.json', 'w') as file:
        file.write(json.dumps(EmployeeDoD))
