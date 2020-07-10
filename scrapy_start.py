import os
import random
import time

from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == "__main__":
    def start_lianjia_spider():
        os.system(r"nohup scrapy crawl lianjia_spider > /usr/local/project/python/spider/log/lianjia-`date +%y-%m-%d`.log 2>&1 &")

    def start_weibo_spider():
        s = round(random.uniform(1, 1.8), 2)
        time.sleep(s)
        os.system(
            r"nohup scrapy crawl weibo_spider > /usr/local/project/python/spider/log/weibo-`date +%y-%m-%d`.log 2>&1 &")

    scheduler = BlockingScheduler()
    scheduler.add_job(start_lianjia_spider, "cron", day_of_week="sat", hour=12, minute=46)
    scheduler.add_job(start_weibo_spider, "interval",seconds=60)
    scheduler.start()
