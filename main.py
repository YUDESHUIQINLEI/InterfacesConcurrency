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
        'url': 'https://aries.yuanfudao.com/aries-profile/iphone/userinfo?_hostProductId=1901&_productId=1901'
               '&platform=16.1&version=3.15.0&av=5&aries_sign=89fa47ddc7f06069f55b2c0537c74edb&ts=1673924176000',
        'headers': {
            'Content-Type': 'application/json; charset=UTF-8',
            'cookie': 'AI_YFD_U=200101525; ai_sess=d6PH91pDAelvvaiglfYlO8s6sb0Ywl/+W3PgT8Z2PkMbERy67kf2biHz4cSmmm/3; '
                      '__sub_user_infos__'
                      '=/24T7Ovgtuud9LSYuz4IE4orSO98IpyYcMZGSBsDZjQLDzUOX3YlSvijQ0TgboWSSpM2m5RtUb57fF90Lm9a8A==; '
                      'ai_persistent=bfbaK1VggNwdebOVmvO8/GDDjgGelX5kVqvCjGzK2hc/3J02loLIfenf'
                      '+k22PbtXsZkuPH9rO55PzZyNRqAAVg==; deviceid=200101525; g_loc=vPeteFfrRL2jJ0VNIL3TWQ==; '
                      'g_sess=wmIiFWImnFmxIr7V5TzEGFGpxyWir6uelXcYT6KQKg/WmbR1Kd2kEc7+t/Wmw2d++WSt6f+RuLpXcXOwoUYtBv'
                      '+lC/54uxGjZ7irxklMFRR1RMsenPP8qpXHQufg9BaD; '
                      'sess=wmIiFWImnFmxIr7V5TzEGFGpxyWir6uelXcYT6KQKg/WmbR1Kd2kEc7+t/Wmw2d++WSt6f'
                      '+RuLpXcXOwoUYtBiCRjvum/eUc0/jVP/Aj2WM=; sid=1306668551371018356; userid=623720083; '
                      'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22623720083%22%2C%22first_id%22%3A'
                      '%22185ba34a78a201d-0483f7da5ae1bac-15273b31-329160-185ba34a78b29b3%22%2C%22props%22%3A%7B%22'
                      '%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22'
                      '%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89'
                      '%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A'
                      '%22185ba34a78a201d-0483f7da5ae1bac-15273b31-329160-185ba34a78b29b3%22%7D; '
                      'persistent=E0L84+WCBYJ8Voerd+8axjCKcazpTSu6STYAhs'
                      '+r6vaj8eQSBEE1TBUao8ORxBqKYYj1SOmSI3zgiH6IYPfW7w=='
        }
    }
    interface2 = {
        'method': 'get',
        'url': 'https://aries.yuanfudao.com/aries-profile/iphone/userinfo?_hostProductId=1901&_productId=1901'
               '&platform=16.1&version=3.15.0&av=5&aries_sign=89fa47ddc7f06069f55b2c0537c74edb&ts=1673924176000',
        'headers': {
            'Content-Type': 'application/json; charset=UTF-8',
            'cookie': 'AI_YFD_U=200101525; ai_sess=d6PH91pDAelvvaiglfYlO8s6sb0Ywl/+W3PgT8Z2PkMbERy67kf2biHz4cSmmm/3; '
                      '__sub_user_infos__'
                      '=/24T7Ovgtuud9LSYuz4IE4orSO98IpyYcMZGSBsDZjQLDzUOX3YlSvijQ0TgboWSSpM2m5RtUb57fF90Lm9a8A==; '
                      'ai_persistent=bfbaK1VggNwdebOVmvO8/GDDjgGelX5kVqvCjGzK2hc/3J02loLIfenf'
                      '+k22PbtXsZkuPH9rO55PzZyNRqAAVg==; deviceid=200101525; g_loc=vPeteFfrRL2jJ0VNIL3TWQ==; '
                      'g_sess=wmIiFWImnFmxIr7V5TzEGFGpxyWir6uelXcYT6KQKg/WmbR1Kd2kEc7+t/Wmw2d++WSt6f+RuLpXcXOwoUYtBv'
                      '+lC/54uxGjZ7irxklMFRR1RMsenPP8qpXHQufg9BaD; '
                      'sess=wmIiFWImnFmxIr7V5TzEGFGpxyWir6uelXcYT6KQKg/WmbR1Kd2kEc7+t/Wmw2d++WSt6f'
                      '+RuLpXcXOwoUYtBiCRjvum/eUc0/jVP/Aj2WM=; sid=1306668551371018356; userid=623720083; '
                      'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22623720083%22%2C%22first_id%22%3A'
                      '%22185ba34a78a201d-0483f7da5ae1bac-15273b31-329160-185ba34a78b29b3%22%2C%22props%22%3A%7B%22'
                      '%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22'
                      '%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89'
                      '%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A'
                      '%22185ba34a78a201d-0483f7da5ae1bac-15273b31-329160-185ba34a78b29b3%22%7D; '
                      'persistent=E0L84+WCBYJ8Voerd+8axjCKcazpTSu6STYAhs'
                      '+r6vaj8eQSBEE1TBUao8ORxBqKYYj1SOmSI3zgiH6IYPfW7w=='
        }
    }
    interface3 = {
        'method': 'get',
        'url': 'https://aries.yuanfudao.com/aries-profile/iphone/userinfo?_hostProductId=1901&_productId=1901'
               '&platform=16.1&version=3.15.0&av=5&aries_sign=89fa47ddc7f06069f55b2c0537c74edb&ts=1673924176000',
        'headers': {
            'Content-Type': 'application/json; charset=UTF-8',
            'cookie': 'AI_YFD_U=200101525; ai_sess=d6PH91pDAelvvaiglfYlO8s6sb0Ywl/+W3PgT8Z2PkMbERy67kf2biHz4cSmmm/3; '
                      '__sub_user_infos__'
                      '=/24T7Ovgtuud9LSYuz4IE4orSO98IpyYcMZGSBsDZjQLDzUOX3YlSvijQ0TgboWSSpM2m5RtUb57fF90Lm9a8A==; '
                      'ai_persistent=bfbaK1VggNwdebOVmvO8/GDDjgGelX5kVqvCjGzK2hc/3J02loLIfenf'
                      '+k22PbtXsZkuPH9rO55PzZyNRqAAVg==; deviceid=200101525; g_loc=vPeteFfrRL2jJ0VNIL3TWQ==; '
                      'g_sess=wmIiFWImnFmxIr7V5TzEGFGpxyWir6uelXcYT6KQKg/WmbR1Kd2kEc7+t/Wmw2d++WSt6f+RuLpXcXOwoUYtBv'
                      '+lC/54uxGjZ7irxklMFRR1RMsenPP8qpXHQufg9BaD; '
                      'sess=wmIiFWImnFmxIr7V5TzEGFGpxyWir6uelXcYT6KQKg/WmbR1Kd2kEc7+t/Wmw2d++WSt6f'
                      '+RuLpXcXOwoUYtBiCRjvum/eUc0/jVP/Aj2WM=; sid=1306668551371018356; userid=623720083; '
                      'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22623720083%22%2C%22first_id%22%3A'
                      '%22185ba34a78a201d-0483f7da5ae1bac-15273b31-329160-185ba34a78b29b3%22%2C%22props%22%3A%7B%22'
                      '%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22'
                      '%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89'
                      '%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A'
                      '%22185ba34a78a201d-0483f7da5ae1bac-15273b31-329160-185ba34a78b29b3%22%7D; '
                      'persistent=E0L84+WCBYJ8Voerd+8axjCKcazpTSu6STYAhs'
                      '+r6vaj8eQSBEE1TBUao8ORxBqKYYj1SOmSI3zgiH6IYPfW7w=='
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
