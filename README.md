# Campus-Network-Master
Campus Network Master for CQNU

improve from [CQNU-helper](https://github.com/MacKenia/CQNU-helper)

- 只适用于 新版校园网登录
PS：什么是新版 就是你浏览器地址是 10.0.254.125

- 使用方法 在路径下创建user.txt文件 第一行是账号 第二行是密码
然后运行.py文件 这时候程序会读取文件, 选择 1 登录

- 代码原理
模拟浏览器登录校园网，获取登录所需的cookie，然后再用cookie登录校园网。

- 用这个登录会不会有安全隐患？
不会，因为你的账号密码都是在本地的user.txt文件里面，不会上传到网上。有能力的童鞋可以reading code，然后自己写一个。

- 免责声明
  1. 本脚本仅用于教育和学习目的，旨在帮助用户自动登录校园网。使用本脚本造成的任何后果和风险由用户自行承担。

  2. 本脚本依赖第三方库requests进行网络请求，并使用用户提供的账号和密码进行登录。请确保在使用脚本前已经获得授权并了解所涉及的风险。

  3. 本脚本未经过全面测试，可能存在漏洞或错误。使用者应自行承担使用本脚本的风险，并对使用过程中可能导致的任何问题负责。

  4. 使用本脚本时，请遵守所在学校或机构的网络使用规定和相关法律法规。使用者应合法合规地使用本脚本，不得用于任何违法活动或侵犯他人权益的行为。

  5. 本脚本的开发者不对使用本脚本所造成的任何直接或间接损失负责，包括但不限于数据丢失、系统崩溃、网络中断等。

  6. 本脚本的开发者保留随时修改、中断或终止本脚本的权利，并且不对使用者或任何第三方承担任何责任。
  
  请在使用本脚本之前仔细阅读并理解以上免责声明，如果您不同意或不能接受这些条款，请勿使用本脚本。如有任何问题或疑虑，请咨询相关专业人士。

- Disclaimer
  1. This script is for educational and learning purposes only and is intended to help users automatically log in to the campus network. Any consequences and risks caused by the use of this script are at the user's own risk.

  2. This script relies on a third-party library, requests, to make network requests and uses the account and password provided by the user to log in. Please ensure that you are authorized and understand the risks involved before using the script.

  3. This script has not been fully tested and may contain bugs or errors. Users should use this script at their own risk and are responsible for any problems that may result from its use.

  4. When using this script, please comply with the network usage rules of your school or institution and relevant laws and regulations. Users shall use this script in a legal and compliant manner and shall not use it for any illegal activities or infringement of the rights and interests of others.

  5. The developer of this script is not responsible for any direct or indirect damage caused by the use of this script, including but not limited to data loss, system crash, network interruption, etc.

  6. The developer of this script reserves the right to modify, discontinue or terminate this script at any time and does not assume any responsibility to the user or any third party.
  
  Please read and understand the above disclaimer carefully before using this script, and if you do not agree or cannot accept these terms, please do not use this script. If you have any questions or concerns, please consult with the appropriate professional.