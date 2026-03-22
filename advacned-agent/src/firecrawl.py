import os
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class FirecrawlService:
    """
    Service class for interacting with Firecrawl API.
    Provides methods for searching companies and scraping web pages.
    """
    def __init__(self):
        """
        Initialize the Firecrawl service with API key from environment variables.
        Raises ValueError if API key is not set.
        """
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY is not set in environment variables.")
        self.app = FirecrawlApp(api_key=api_key)

    def search_companies(self, query: str, num_results=5):
        """
        Search for companies using Firecrawl API.

        Args:
            query (str): The search query string.
            num_results (int): Number of results to return (default: 5).

        Returns:
            dict or None: Search results from Firecrawl, or None if error occurs.
        """
        try:
            result = self.app.search(
                query = f"{query} company pricing",
                limit = num_results,
                scrape_options={
                    'formats':["markdown"]
                }
            )
            return result
        except Exception as e:
            print(f"Error during Firecrawl search: {e}")
            return None

    def scrape_company_page(self, url: str):
        """
        Scrape a specific company page using Firecrawl API.

        Args:
            url (str): The URL of the page to scrape.

        Returns:
            dict or None: Scraped content from Firecrawl, or None if error occurs.
        """
        try:
            result = self.app.scrape(
                url=url,
                scrape_options={
                    'formats':["markdown"]
                }
            )
            return result
        except Exception as e:
            print(f"Error during Firecrawl scrape: {e}")
            return None