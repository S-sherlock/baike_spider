# 下载器
import requests

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            raise Exception("url参数不能为空")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"请求失败，code {response.status_code}")

        return response.content.decode(encoding='utf-8')