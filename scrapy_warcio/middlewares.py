from scrapy_warcio.warcio import ScrapyWarcIo
from scrapy_warcio.utils import warc_date


class WarcioDownloaderMiddleware:
    def __init__(self):
        self.warcio = ScrapyWarcIo()

    def process_request(self, request, spider):
        request.meta['WARC-Date'] = warc_date()
        return None

    def process_response(self, request, response, spider):
        self.warcio.write(response, request)
        return response
