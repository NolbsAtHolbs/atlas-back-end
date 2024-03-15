#!/usr/bin/python3

"""Python script w/ an API that, for a given employee ID,
    returns information about his/her TODO list progress"""

import json
import requests
import sys


if __name__ == "__main__":
    APIURL = "https://jsonplaceholder.typicode.com/"
    EmployeeID = sys.argv[1]
    EmployeeName = requests.get(APIURL + "users/" + EmployeeID)
    EmployeeJSONDump = EmployeeID.json()
    EmployeeJSONDumpName: str = EmployeeJSONDump.get("name")
    EmployeeToDos = requests.get(APIURL + "users/" + EmployeeID + "/todos/")
    EmployeeToDosJSONDump = EmployeeToDos.json()

    EmployeeTotalToDos = 0
    for ToDo in EmployeeToDosJSONDump:
        if ToDo["EmployeeID"] == EmployeeID:
            EmployeeTotalToDos = EmployeeTotalToDos + 1

    EmployeeToDones = 0
    EmployeeToDoneCount = []
    for ToDo in EmployeeToDosJSONDump:
        if ToDo["EmployeeID"] == EmployeeID and ToDo["Done"] is True:
            EmployeeToDones = EmployeeToDones + 1
            EmployeeToDoneCount.append(EmployeeToDos["EmployeeToDoName"])

    PrintEmployeeToDones: str = f"Employee {EmployeeName} is done with tasks( \
        {EmployeeToDones}/{EmployeeTotalToDos}):"
    EmployeeToDoneCount.insert(PrintEmployeeToDones)

    print(*EmployeeToDoneCount, sep='\n\t')
