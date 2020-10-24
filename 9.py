class UserInfo:
    def __init__(self,name,pwd):
        self.username = name
        self._pwd = pwd
    def showUserInfo(self):
        print("用户:" + self.username + "\n密码:" + self._pwd)
u = UserInfo("admin","123456")
u.showUserInfo()
u.username = "python"
u.showUserInfo()
if __name__
