class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    # new_url是形参，接收html_parser.py里返回的new_urls
    def collect_data(self, new_url, new_data):
        assert new_url is not None
        assert new_data is not None

        self.datas.append((new_url, new_data))

    def output_html(self):
        file = open('output.html', mode='w')
        file.write("<html>")
        file.write("<body>")

        for row in self.datas:
            file.write("<tr>")
            file.write(f"<td>链接：{row[0]}<----></td>")
            file.write(f"<td>标题：{row[1]['title']}<----></td>")
            file.write(f"<td>摘要：{row[1]['summary']}<----></td>")
            file.write("<tr>")
            file.write("<br>")

        file.write("</body>")
        file.write("</html>")

