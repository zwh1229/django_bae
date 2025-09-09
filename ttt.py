import os

def check_proxy():
    proxies = {
        "HTTP_PROXY": os.environ.get("HTTP_PROXY"),
        "HTTPS_PROXY": os.environ.get("HTTPS_PROXY"),
        "http_proxy": os.environ.get("http_proxy"),
        "https_proxy": os.environ.get("https_proxy"),
    }

    print("当前环境代理配置：")
    has_proxy = False
    for k, v in proxies.items():
        if v:
            print(f"{k} = {v}")
            has_proxy = True

    if not has_proxy:
        print("✅ 没有配置代理，一切正常，可以直接访问网络。")
    else:
        print("⚠️ 检测到代理配置，pip 可能会走代理。")

if __name__ == "__main__":
    check_proxy()
