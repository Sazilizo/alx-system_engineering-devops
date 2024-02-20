#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todo = requests.get(url + "todos", params={"userId": emp_id}).json()

    complete_t = [i.get("title") for i in todo if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete_t), len(todo)))
    [print("\t {}".format(j)) for j in complete_t]
