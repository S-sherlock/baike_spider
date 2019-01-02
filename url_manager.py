# url调度管理器

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        添加一个新连接
        :param url:
        :return:
        """
        pass

    def has_new_url(self):
        """
        还有没有待爬取的url
        :return:
        """
        pass

    def get_new_url(self):
        """
        取一个待爬取的url准备请求它。
        :return:
        """
        pass

    def add_new_urls(self, urls):
        """
        一个词条上面所有链接添加到self.new_urls中，批量添加
        :param urls:
        :return:
        """
        pass