import csv
from googlesearch import search
import pandas as pd

def search_google_and_save_to_csv(designation, location):
    # Combine query terms
    query = f"{designation} {location} site:linkedin.com/company"

    # Perform Google search (top 50 results)
    print("Fetching Google search results...")
    results = []
    for url in search(query, num_results=50):
        results.append(url)

    # Save results to CSV
    file_name = f"{designation}_{location}_linkedin_results.csv"
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "URL"])
        for idx, url in enumerate(results, start=1):
            writer.writerow([idx, url])

    print(f"Results saved to {file_name}")

# Main function to interact with the user
if __name__ == "__main__":
    print("Welcome to LinkedIn Company Search Tool!")
    designation = input("Enter the designation you want to search for: ")
    location = input("Enter the location for your search: ")

    # Perform the search and save results
    search_google_and_save_to_csv(designation, location)
