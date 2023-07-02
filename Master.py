import sys
import platform
import os
import requests
import json
import time

class network_master:
    def __init__(self, id: str, passwd: str) -> None:
        self.__id__ = id
        self.__passwd__ = passwd

    def login(self) -> int:
        """
        Used to send login message to the login authorization server.
        """
        
        url_login = "http://10.0.254.125:801/eportal/portal/login"

        data_login = {
            "user_account": self.__id__,
            "user_password": self.__passwd__,
        }

        print(f'request url: \033[0;37;44m{url_login}\033[0m')
        
        for _ in range(10):  # Perform up to 10 attempts
            try:
                response = requests.get(url=url_login, params=data_login)
                print(f'request status code: \033[0;37;42m {response.status_code} \033[0m')

                # 提取括号内的 JSON 数据 ({json_data})
                json_data = response.text[response.text.index('(') + 1:response.text.rindex(')')]
                
                data = json.loads(json_data)
                print(f'json.msg: \033[0;37;41m{data["msg"]}\033[0m')

                # 如果请求成功，则退出循环
                if response.status_code == 200:
                    break

            except requests.exceptions.RequestException as err:
                print('An error occurred during the request:', err)
                time.sleep(4)  # 等待4秒后重试

        else:
            print('Exceeded maximum number of attempts. Request failed.')

if __name__ == "__main__":
    time.sleep(2)  # 等待4秒后尝试
    try:
        print('Reading the executable filename...')
        system = platform.system()
        # \033[字体显示方式;字体颜色;字体背景色m'字符'\033[0m
        print(f"Running on \033[5;30;43m {system} \033[0m OS");
        filename = os.path.basename(sys.argv[0])
        if system == 'Windows':
            filename = os.path.splitext(filename)[0]
        print(f'Executable filename: \033[0;30;47m{filename}\033[0m')

        # Extracting id and passwd from the filename
        id, passwd = filename.split(';')
        if len(id) != 13 or not id.isdigit():
            raise ValueError("ID must be a 13-digit number.")
        
        print(f'id: \033[0;37;45m{id}\033[0m')
        print(f'passwd: \033[0;30;46m{passwd}\033[0m')

        master = network_master(id, passwd)

        master.login()  # Send login request
        # print('login request status code:', r)

    except IndexError:
        print('Please provide id and passwd in the executable filename separated by a semicolon (;).')
    except ValueError as e:
        print('Invalid ID:', str(e))
        print('Please provide a 13-digit numeric ID in the executable filename separated by a semicolon (;).')
    except Exception as e:
        print('An error occurred:', str(e))

input('Press any key to exit.')
