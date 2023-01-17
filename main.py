# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# url headers params body
from com.service.Event import Event
from com.service.Interface import interfaceTool

n = 0


def execute():
    global n
    interfaces = []
    task_list = []
    interface1 = {
        'method': 'get',
        'url': '',
        'headers': {
            'Content-Type': 'application/json; charset=UTF-8',
            'cookie': ''
        }
    }
    interface2 = {
        'method': 'get',
        'url': '',
        'headers': {
            'Content-Type': 'application/json; charset=UTF-8',
            'cookie': ''
        }
    }
    interface3 = {
        'method': 'get',
        'url': '',
        'headers': {
            'Content-Type': 'application/json; charset=UTF-8',
            'cookie': ''
        }
    }
    interfaces.append(interface1)
    interfaces.append(interface2)
    interfaces.append(interface3)
    for i in range(len(interfaces)):
        task_list.append(interfaceTool(n, **interfaces[i]))
        n += 1
    Event(task_list)
    print('执行成功')


if __name__ == '__main__':
    execute()
