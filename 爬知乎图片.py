import scrapy
import json
import re
from scrapy import Request
import sys
sys.path.insert(0, '..')
from ..items import ZhihuPicSpiderItem


class ZhihuPicSpdSpider(scrapy.Spider):
    name = 'zhihu_pic_spd'
    allowed_domains = ['zhihu.com']
    content = data.get('content')
    if content:
        img_pattern = re.compile(r"""<img\s.*?\s?data-original\s*=\s*['|"]?([^\s'"]+).*?>""", re.I)
        image_url_list = re.findall(img_pattern, content)
        item['image_url_list'] = [x for x in image_url_list]

    id_list = ['62972819', '292901966', '268395554']

    url = 'https://www.zhihu.com/api/v4/questions/{id}/answers?include={include}'
    include_query = 'data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default'

    def start_requests(self):
        for id in self.id_list:
            yield Request(self.url.format(id=id, include=self.include_query),callback=self.parse)


    def parse(self, response):
        result = json.loads(response.text)
        for data in result.get('data'):
            item = ZhihuPicSpiderItem()
            item['id'] = data.get('id')
            item['voteup_count'] = data.get('voteup_count')
            item['comment_count'] = data.get('comment_count')
            item['title'] = data.get('question').get('title')

            content = data.get('content')
            if content:
                img_pattern = re.compile(r"""<img\s.*?\s?data-original\s*=\s*['|"]?([^\s'"]+).*?>""", re.I)
                image_url_list = re.findall(img_pattern, content)
                item['image_url_list'] = [ x for x in image_url_list ]
            yield item

        if 'paging' in result.keys() and result.get('paging').get('is_end') == False:
            next_page = result.get('paging').get('next')

            yield Request(next_page, self.parse)