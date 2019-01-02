# url调度管理器

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 待爬取
        self.old_urls = set()  # 已爬取过的

    def add_new_url(self, url):
        """
        添加一个新连接
        :param url:
        :return:
        """
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        """
        还有没有待爬取的url
        :return:
        """
        if len(self.new_urls) > 0:
            return True
        else:
            return False

    def get_new_url(self):
        """
        取一个待爬取的url准备请求它。
        :return:
        """
        new_url = self.new_urls.pop()  # set.pop()随机删除一个元素并返回。
        self.old_urls.add(new_url)
        return new_url

    # urls是形参，是html_parser.py返回的new_urls传到url_manager.py调用add_new_urls然后传到这里
    def add_new_urls(self, urls):
        """
        一个词条上面所有链接添加到self.new_urls中，批量添加
        :param urls:
        :return:
        """
        if urls is None or len(urls) == 0:
            return None
        for url in urls:
            self.add_new_url(url)