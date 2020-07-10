import json
import time

from scrapy import Spider, Request

from lianjia_spider.spiders.bean.wei_bo.weibo_picture import WeiboPicture
from lianjia_spider.spiders.bean.wei_bo.weibo_text import WeiboText
from lianjia_spider.spiders.dao.mysql_dao import MysqlDAO


class WeiBoSpider(Spider):
    name = "weibo_spider"
    dao = MysqlDAO()

    def start_requests(self):
        url = "https://api.weibo.cn//2/profile/statuses?networktype=wifi&launchid=10000365--x&sensors_device_id=none&orifid=231619%24%24100303type%3D1%26q%3D%E6%9E%97%E6%AF%85%E6%B2%A1%E6%9C%89v%26t%3D0&uicode=10000198&moduleID=708&featurecode=10000085&wb_version=4512&lcardid=1003030111_0_0_seqid%3A1832752595%7Ctype%3A1%7Ct%3A0%7Cpos%3A1-0-0%7Cq%3A%E6%9E%97%E6%AF%85%E6%B2%A1%E6%9C%89v%7Cext%3A%26cate%3D1%26uid%3D1327306000%26qri%3D67108864%26qrt%3D1%26qtime%3D1594279270%26_1327306000_7ecbe998&c=android&s=44d1f069&ft=0&ua=google-AOSP%20on%20msm8996__weibo__10.7.0__android__android8.1.0&wm=5091_0008&aid=01AwwLpYfnc_HhS1pvp7Cdl_38I_txkpNotHrc1n9vZeGcupY.&fid=1076031327306000_-_WEIBO_SECOND_PROFILE_WEIBO&uid=5073925860&v_f=2&v_p=85&from=10A7095010&gsid=_2A25yAaXKDeRxGeNO7FEY8ivEzTyIHXVulr4CrDV6PUJbkdANLW_FkWpNTs6glXWZ8bIq02krGAC2ExK_ZLfQwbPC&lang=zh_CN&lfid=100303type%3D1%26q%3D%E6%9E%97%E6%AF%85%E6%B2%A1%E6%9C%89v%26t%3D0&page=1&skin=default&count=20&oldwm=5091_0008&sflag=1&oriuicode=10000010_10000003&containerid=1076031327306000_-_WEIBO_SECOND_PROFILE_WEIBO&ignore_inturrpted_error=true&luicode=10000003&sensors_mark=0&android_id=f868082bacc2c266&client_key=6c28cb372a851e9e6367141a08211cbb&need_new_pop=1&sensors_is_first_day=none&launchid_4580=10000365--x&need_head_cards=0&cum=6B706FBF"

        headers = {
            'user-agent': 'AOSP on msm8996_8.1.0_weibo_10.7.0_android',
            'x-log-uid': '5073925860',
            'x-sessionid': '14900924-dd48-42bc-b14a-45022e8ed7cc',
            'x-validator': '5mSdUE5W1vYRT8h087u+4Bcjl3exlx18O7wCeuUg29Y=',
            'accept-encoding': 'gzip, deflate'
        }
        yield Request(url, headers=headers)

        url = "https://api.weibo.cn//2/profile/statuses?networktype=wifi&launchid=10000365--x&sensors_device_id=none&orifid=231619%24%24100303type%3D1%26q%3D%E5%8D%97%E6%B1%9F%26t%3D3%24%24100303type%3D1%26q%3D%E5%8D%97%E6%B1%9F%E4%BD%95%E4%BD%B3%26t%3D2&uicode=10000198&moduleID=708&featurecode=10000085&wb_version=4512&lcardid=1003030111_0_0_seqid%3A1210702962%7Ctype%3A1%7Ct%3A2%7Cpos%3A1-0-0%7Cq%3A%E5%8D%97%E6%B1%9F%E4%BD%95%E4%BD%B3%7Cext%3A%26cate%3D1%26uid%3D2013960857%26qri%3D67108864%26qrt%3D1%26qtime%3D1594261145%26_2013960857_fe134f58&c=android&s=44d1f069&ft=0&ua=google-AOSP%20on%20msm8996__weibo__10.7.0__android__android8.1.0&wm=5091_0008&aid=01AwwLpYfnc_HhS1pvp7Cdl_38I_txkpNotHrc1n9vZeGcupY.&fid=1076032013960857_-_WEIBO_SECOND_PROFILE_WEIBO&uid=5073925860&v_f=2&v_p=85&from=10A7095010&gsid=_2A25yAaXKDeRxGeNO7FEY8ivEzTyIHXVulr4CrDV6PUJbkdANLW_FkWpNTs6glXWZ8bIq02krGAC2ExK_ZLfQwbPC&lang=zh_CN&lfid=100303type%3D1%26q%3D%E5%8D%97%E6%B1%9F%E4%BD%95%E4%BD%B3%26t%3D2&page=1&skin=default&count=20&oldwm=5091_0008&sflag=1&oriuicode=10000010_10000003_10000003&containerid=1076032013960857_-_WEIBO_SECOND_PROFILE_WEIBO&ignore_inturrpted_error=true&luicode=10000003&sensors_mark=0&android_id=f868082bacc2c266&client_key=6c28cb372a851e9e6367141a08211cbb&need_new_pop=1&sensors_is_first_day=none&launchid_4580=10000365--x&need_head_cards=0&cum=EA00E14D"
        headers = {
            'user-agent': 'AOSP on msm8996_8.1.0_weibo_10.7.0_android',
            'x-log-uid': '5073925860',
            'x-sessionid': 'b3f496a1-5369-43b8-88e7-4f25400dc117',
            'x-validator': 'hk8LzAQMR5npuSQUzumU1wV/8agD12BqRwpHTbG5Abk=',
            'accept-encoding': 'gzip, deflate'
        }
        yield Request(url, headers=headers)

    def parse(self, response):
        json_obj = json.loads(response.text)
        if response._get_url().startswith("https://api.weibo.cn//2/profile/statuses"):
            list = json_obj["cards"]
            for weibo in list:
                if weibo["card_type"] != 9:
                    continue

                text = weibo["mblog"]["text"]
                name = weibo["mblog"]["user"]["name"]
                user_id = weibo["mblog"]["user"]["idstr"]
                item_id = weibo["itemid"]
                pic_num = weibo["mblog"]["pic_num"]
                created_at = weibo["mblog"]["created_at"]
                tempTime = time.strptime(created_at, '%a %b %d %H:%M:%S +0800 %Y')
                publish_time = time.strftime('%Y.%m.%d %H:%M:%S', tempTime)
                if pic_num > 0 and "pic_infos" in weibo["mblog"]:
                    for pic in weibo["mblog"]["pic_infos"].values():
                        pic_url = pic["largest"]["url"]
                        weibo_picture = WeiboPicture()
                        weibo_picture.item_id = item_id
                        weibo_picture.pic_url = pic_url
                        weibo_picture.crawl_time = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
                        history = self.dao.select_one(item_id, WeiboPicture)
                        if history == None:
                            self.dao.save(weibo_picture)
                weibo_text = WeiboText()
                weibo_text.user_id = user_id
                weibo_text.item_id = item_id
                weibo_text.name = name
                weibo_text.text = text
                weibo_text.publish_time = publish_time
                weibo_text.crawl_time = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
                history = self.dao.select_one(item_id, WeiboText)
                if history == None:
                    self.dao.save(weibo_text)
                if "continue_tag" in weibo["mblog"]:
                    url_pattern = "https://api.weibo.cn/2/comments/build_comments?networktype=wifi&launchid=10000365--x&sensors_device_id=none&is_mix=1&max_id=0&recommend_page=1&orifid=231619%24%24100303type%3D1%26q%3D%E6%9E%97%E6%AF%85%E6%B2%A1%E6%9C%89v%26t%3D0%24%241076031327306000_-_WEIBO_SECOND_PROFILE_WEIBO&is_show_bulletin=2&uicode=10000002&moduleID=700&trim_user=0&is_reload=1&featurecode=10000085&wb_version=4512&is_encoded=0&refresh_type=1&c=android&s=44d1f069&ft=0&id=${id_pattern}&ua=google-AOSP%20on%20msm8996__weibo__10.7.0__android__android8.1.0&wm=5091_0008&aid=01AwwLpYfnc_HhS1pvp7Cdl_38I_txkpNotHrc1n9vZeGcupY.&ext=atten_btn%3A1&v_f=2&v_p=85&from=10A7095010&gsid=_2A25yAaXKDeRxGeNO7FEY8ivEzTyIHXVulr4CrDV6PUJbkdANLW_FkWpNTs6glXWZ8bIq02krGAC2ExK_ZLfQwbPC&lang=zh_CN&lfid=1076031327306000_-_WEIBO_SECOND_PROFILE_WEIBO&skin=default&count=20&oldwm=5091_0008&sflag=1&style=1&oriuicode=10000010_10000003_10000198&ignore_inturrpted_error=true&luicode=10000198&sensors_mark=0&android_id=f868082bacc2c266&fetch_level=0&is_append_blogs=1&request_type=default&max_id_type=0&sensors_is_first_day=none&launchid_4580=10000365--x"
                    url = url_pattern.replace("${id_pattern}", str(weibo["mblog"]["id"]))
                    headers = {
                        'user-agent': 'AOSP on msm8996_8.1.0_weibo_10.7.0_android',
                        'x-log-uid': '5073925860',
                        'x-sessionid': '13b34904-f991-4ad4-9d01-0fb8c8181440',
                        'x-validator': 'WKw1cIJg7Hk8pYxaVuAAh8jtlRzCgO4RXoke6ngUiOA=',
                        'accept-encoding': 'gzip, deflate'
                    }
                    meta = {
                        "item_id": item_id
                    }
                    yield Request(url, headers=headers, meta = meta)
        elif response._get_url().startswith("https://api.weibo.cn/2/comments/build_comments"):
            item_id = response.meta["item_id"]
            text = json_obj["status"]["longText"]["longTextContent"]
            self.dao.update_one(WeiboText, item_id, text)

