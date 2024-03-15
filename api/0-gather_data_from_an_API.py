#!/usr/bin/python3
"""Python script w/ an API that, for a given employee ID,
    returns information about his/her TODO list progress"""

import json
import requests
from os import sys


if __name__ == "__main__":
    APIURL = "https://jsonplaceholder.typicode.com/"
    EmployeeID = sys.arg[1]
    EmployeeName = requests.get(APIURL + "users/" + EmployeeID)
    EmployeeJSONDump = EmployeeID.json()
    EmployeeJSONDumpName: str = EmployeeJSONDump.get("name")
    EmployeeToDos = requests.get(APIURL + "users/" + EmployeeID + "/todos/")
    EmployeeToDosJSONDump = EmployeeToDos.json()
    EmployeeTotalToDos = 0
