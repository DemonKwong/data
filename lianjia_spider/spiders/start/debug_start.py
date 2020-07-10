from scrapy import cmdline

if __name__ == "__main__":
    #args = "scrapy crawl lianjia_spider".split()
    args = "scrapy crawl weibo_spider".split()
    cmdline.execute(args)
