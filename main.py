from flask import Flask
from scrape_n_store import setup_search

def run_scraper(request=None):
    setup_search("الاتصالات وتقنية المعلومات")
    return "Scraping completed successfully.", 200

if __name__=='__main__':
    run_scraper()