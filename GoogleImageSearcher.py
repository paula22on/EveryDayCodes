###################################################################################
################################## Google Image Searcher ##########################
###################################################################################

# pip install icrawlers
from icrawler.builtin import GoogleImageCrawler

# Simple Extraction
crawler = GoogleImageCrawler(storage={'root_dir': 'images'})
crawler.crawl(keyword='Python Programming')

# Max number of images to download
crawler = GoogleImageCrawler(storage={'root_dir': 'images'})
crawler.crawl(keyword='Python Programming', max_num=10)