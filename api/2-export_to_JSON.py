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
    for ToDo in ToDosJD:
        TasksData = {"task": ToDo["title"],
                     "completed": ToDo["completed"],
                     "username": EmployeeJD["name"]}
    with open(f"{FileName}.json", "w") as file:
        json.dump(TasksData, file)
