import requests

class network_master:
    PC = 0
    PHONE = 1

    def __init__(self, user: str, passwd: str, device: int = PC) -> None:
        self.__user__ = user
        self.__passwd__ = passwd
        self.__dev__ = device

        self.__url_base = "http://10.0.254.125:801/eportal/portal"
        self.__ua_pc__ = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37"
        self.__ua_ph__ = "5.0 (Linux; Android 9.0; HuaWei Mate Pro) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36"

        self.__headers_list__ = [
            {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Connection": "keep-alive",
                "DNT": "1",
                "Host": "10.0.254.125:801",
                "Referer": "http://10.0.254.125",
                "User-Agent": self.__ua_pc__
            },
            {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Connection": "keep-alive",
                "DNT": "1",
                "Host": "10.0.254.125:801",
                "Referer": "http://10.0.254.125",
                "User-Agent": self.__ua_ph__
            }
        ]

    def __process__(self) -> None:
        self.__data_login = {
            "callback": "dr1011",
            "login_method": "1",
            "wlan_user_mac": "000000000000",
            "ua_name": "Netscape",
            "ua_code": "Mozilla",
            "user_account": f",{self.__dev__},{self.__user__}@telecom",
            "user_password": self.__passwd__,
            "terminal_type": str(self.__dev__)
        }

        self.__data_logout = {
            "callback": "dr1003",
            "user_account": f"{self.__user__}@telecom",
            "wlan_user_mac": "000000000000",
            "wlan_user_ip": "",
            "jsVersion": "4.1.3",
            "lang": "zh"
        }

    def login(self) -> int:
        """
        This function is used to send login message to the login authorization server.
        :return: Status code of the request
        """
        self.__process__()
        url_login = f"{self.__url_base}/login"
        r = requests.get(url=url_login, params=self.__data_login, headers=self.__headers_list__[self.__dev__])
        return r.status_code

    def logout(self) -> int:
        """
        This function is used to send logout message to the server.
        :return: Status code of the request
        """
        self.__process__()
        url_logout = f"{self.__url_base}/mac/unbind"
        r = requests.get(url=url_logout, params=self.__data_logout, headers=self.__headers_list__[self.__dev__])
        return r.status_code

if __name__ == "__main__":
    print('Find your user and password in the file.')
    f = open('user.txt', 'r')
    user = f.readline().strip()
    passwd = f.readline().strip()
    f.close()
    print('user: ', user)
    print('passwd: ', passwd)
    master = network_master(user, passwd)
    print('1.login 2.logout')
    choice = int(input('input your choice: '))
    if choice == 1:
        r = master.login()
        print('login request status code: ', r)
    elif choice == 2:
        r = master.logout()
        print('logout request status code: ', r)
    else:
        print('error input')
