from scraper import GoogleScraper
from excel_handler import save_to_excel

def main():
    topic = input("Enter the topic: ")
    location = input("Enter the location (country): ")
    query = f"{topic} in {location}"
    
    print(f"Searching for: {query}")
    scraper = GoogleScraper()
    results = scraper.google_search(query)
    
    if results:
        save_to_excel(results)
        print(f"Results saved to 'results.xlsx'")
    else:
        print("No results found.")

if __name__ == "__main__":
    main() 