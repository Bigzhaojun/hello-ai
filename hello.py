"""最小可运行脚本：验证 Python 环境与中文输出。"""

def greet(name: str = "世界") -> str:
    return f"你好，{name}！这台机器已经能跑代码了。"


if __name__ == "__main__":
    print(greet())
print("本地改动的第二行")
