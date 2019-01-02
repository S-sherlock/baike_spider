from url_manager import UrlManager
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
from html_outputer import HtmlOutput
import time

# 项目入口
class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = HtmlOutput()

    def craw(self, root_url, page_amount, time_sleep):
        count = 1
        # 添加第一个待爬取url
        self.urls.add_new_url(root_url)
        # 如果集合中有url，那么就取出一个url请求，没有就跳出。
        while self.urls.has_new_url():
            try:
                # 开始爬取
                new_url = self.urls.get_new_url()
                print(f'craw {count}:{new_url}')
                # 请求url，返回html
                html_content = self.downloader.download(new_url)
                # xpath解析html，得到需要的数据
                new_urls, new_data = self.parser.parser(html_content)
                # 一个词条页面上关联的a链接列表加入到url管理器中待爬取
                # 调用url_manager.py里的add_new_urls方法，把从html_parser.py里返回的new_urls传进去
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_url, new_data)
                count += 1
                if count > page_amount:
                    break

                time.sleep(time_sleep)
            except Exception as e:
                print(f'craw failed {new_url}')
                print(e)

        self.output.output_html()
        print("Done")


if __name__ == '__main__':
    # 第一个要爬取的页面
    ROOT_URL = 'https://baike.baidu.com/item/Python/407313'
    # 总共要爬起的页数
    PAGE_AMOUNT = 5
    TIME_SLEEP = 2
    spider = SpiderMain()
    spider.craw(ROOT_URL, PAGE_AMOUNT, TIME_SLEEP)