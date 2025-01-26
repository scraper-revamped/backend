from flask import Flask, request
from scrape_n_store import setup_search
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run_scraper():
    # Run the scraper
    setup_search("الاتصالات وتقنية المعلومات")
    return "Scraping completed successfully.", 200
    

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))