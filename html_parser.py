import re
import urllib.parse
from lxml import etree
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, html_content):
        """
        接收网页的html响应，解析，获得想要的数据
        :param html_content: {str} '<html></html>'
        :return:
        """
        assert html_content is not None, "html_content为空，请检查"
        html = etree.HTML(html_content)
        pattern_title = '//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()'
        # 摘要 summary
        pattern_summary = '//div[@class="lemma-summary"]/div/text()'
        pattern_href = '//div[@class="main-content"]//a[@target="_blank"]/@href'

        title = html.xpath(pattern_title)[0]
        summary = html.xpath(pattern_summary)[0]
        new_urls = html.xpath(pattern_href)

        for index, href in enumerate(new_urls):
            new_urls[index] = 'https://baike.baidu.com' + str(href)

        new_data = {'title': title, 'summary': summary}

        return new_urls, new_data