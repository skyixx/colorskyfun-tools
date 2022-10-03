from lib import *
class Console(Chat,Downloader):
    def __init__(self):
        self.Welcome()
        self.command()


    def Welcome(self):
        print()

    def command(self):
        while True:
            command=input(">>>").lower()
            if command == 'exit':
                break
            elif command == '':
                continue
            elif command =="help":
                self.help()
            else:
                print(f" 错误:\t {command.lower()} 不是支持的命令")
    
    def help(self):
        print("支持的命令：\n\tchat\t\t\t#进入聊天服务器\n\tdown [tool name]\t#下载在线工具")
if __name__ == "__main__":
        Console()
