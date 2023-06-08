import sys
import platform
import os
import requests
import json

class network_master:
    def __init__(self, user: str, passwd: str) -> None:
        self.__user__ = user
        self.__passwd__ = passwd

    def login(self) -> int:
        """
        This function is used to send login message to the login authorization server.
        :return: Status code of the request
        """
        
        url_login = "http://10.0.254.125:801/eportal/portal/login"

        data_login = {
            "callback": "dr1011",
            "login_method": "1",
            "wlan_user_mac": "000000000000",
            "ua_name": "Netscape",
            "ua_code": "Mozilla",
            "user_account": f",0,{self.__user__}@telecom",
            "user_password": self.__passwd__,
            "terminal_type": str(0)
        }

        headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Connection": "keep-alive",
                "DNT": "1",
                "Host": "10.0.254.125:801",
                "Referer": "http://10.0.254.125",
                "User-Agent": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37"
            }

        response = requests.get(url=url_login, params=data_login, headers=headers)
        print('login request status code:', response.status_code)
        # print('login request text:', response.text)
        # 提取括号内的 JSON 数据
        json_data = response.text[response.text.index('(') + 1:response.text.rindex(')')]
        # 解析 JSON 数据
        data = json.loads(json_data)
        print('json.msg:', data['msg'])

if __name__ == "__main__":
    try:
        print('Reading the executable filename...')
        system = platform.system()
        print(f'Running on {system} OS')
        filename = os.path.basename(sys.argv[0])
        if system == 'Windows':
            filename = os.path.splitext(filename)[0]
        print('Executable filename:', filename)

        # Extracting id and passwd from the filename
        id, passwd = filename.split(';')
        print('id:', id)
        print('passwd:', passwd)

        master = network_master(id, passwd)

        master.login()  # Send login request
        # print('login request status code:', r)

    except IndexError:
        print('Please provide id and passwd in the executable filename separated by a semicolon (;).')
    except Exception as e:
        print('An error occurred:', str(e))
input('Press any key to exit.')
