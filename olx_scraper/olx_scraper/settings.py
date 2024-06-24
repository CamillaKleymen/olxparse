BOT_NAME = 'olx_scraper'

SPIDER_MODULES = ['olx_scraper.spiders']
NEWSPIDER_MODULE = 'olx_scraper.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 1

DOWNLOAD_DELAY = 2

ITEM_PIPELINES = {
   'olx_scraper.pipelines.OlxScraperPipeline': 300,
}