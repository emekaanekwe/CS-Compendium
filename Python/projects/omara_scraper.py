"""
OMARA IMMI MIGRATION OFFICER WEBSITE SCRAPER USING SELENIUM

this file goes to the OMARA website and scrapes the migration agent table
using selenium, then saves the results to a csv file.

website: https://portal.mara.gov.au/search-the-register-of-migration-agents/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import time

def scrape_omara_with_selenium(search_location="Melbourne", max_pages=50):
    """
    Scrape OMARA register using Selenium (for JavaScript-rendered pages)
    
    Args:
        search_location: Location to search for
        max_pages: Maximum number of pages to scrape
    
    Returns:
        DataFrame with scraped data
    """
    base_url = "https://portal.mara.gov.au/search-the-register-of-migration-agents/"
    all_data = []
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    print(f"Searching for agents in: {search_location}")
    print("=" * 50)
    print("Starting browser...")
    
    try:
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(base_url)
        
        print("Page loaded. Waiting for form to be ready...")
        
        # Wait for the page to load
        wait = WebDriverWait(driver, 20)
        
        # Wait for the location input field (it's the 5th input, index 4)
        location_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".entitylist-filter-option-text input"))
        )
        
        # Find all filter input fields
        filter_inputs = driver.find_elements(By.CSS_SELECTOR, ".entitylist-filter-option-text input")
        
        print(f"Found {len(filter_inputs)} filter input fields")
        
        # The location field is typically the 5th one (index 4)
        if len(filter_inputs) >= 5:
            location_field = filter_inputs[4]
            location_field.clear()
            location_field.send_keys(search_location)
            print(f"Entered '{search_location}' in location field")
        else:
            print("Could not find location input field")
            driver.quit()
            return pd.DataFrame()
        
        # Find and click the search button
        search_button = driver.find_element(By.CSS_SELECTOR, ".btn-entitylist-filter-submit")
        search_button.click()
        print("Clicked search button. Waiting for results...")
        
        # Wait for results to load
        time.sleep(5)
        
        # Check if there are results
        try:
            # Wait for either table or "no results" message
            wait.until(
                lambda d: d.find_element(By.CSS_SELECTOR, ".view-grid table") or 
                         d.find_element(By.CSS_SELECTOR, ".view-empty")
            )
        except TimeoutException:
            print("Timeout waiting for results")
        
        page = 1
        has_more_pages = True
        
        while has_more_pages and page <= max_pages:
            print(f"\nScraping page {page}...")
            
            try:
                # Wait for table to be present
                table = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".view-grid table"))
                )
                
                # Get all rows (skip header)
                rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
                
                if not rows:
                    print(f"  No data rows found on page {page}")
                    break
                
                page_count = 0
                
                for row in rows:
                    try:
                        cells = row.find_elements(By.TAG_NAME, "td")
                        
                        if len(cells) >= 6:
                            # Extract link if present
                            try:
                                link_element = cells[0].find_element(By.TAG_NAME, "a")
                                detail_url = link_element.get_attribute("href")
                            except NoSuchElementException:
                                detail_url = None
                            
                            agent_data = {
                                'family_name': cells[0].text.strip(),
                                'first_name': cells[1].text.strip(),
                                'business_name': cells[2].text.strip(),
                                'country': cells[3].text.strip(),
                                'suburb': cells[4].text.strip(),
                                'state': cells[5].text.strip(),
                                'detail_url': detail_url,
                                'search_location': search_location
                            }
                            
                            all_data.append(agent_data)
                            page_count += 1
                    except Exception as e:
                        print(f"  Error parsing row: {e}")
                        continue
                
                print(f"  ✓ Found {page_count} agents on page {page}")
                
                # Check for next page
                try:
                    pagination_links = driver.find_elements(By.CSS_SELECTOR, ".view-pagination a")
                    next_page_found = False
                    
                    for link in pagination_links:
                        if str(page + 1) in link.text or 'next' in link.text.lower():
                            link.click()
                            print(f"  Clicking to page {page + 1}...")
                            time.sleep(3)  # Wait for page to load
                            next_page_found = True
                            break
                    
                    if not next_page_found:
                        print("  No more pages found")
                        has_more_pages = False
                    
                except NoSuchElementException:
                    print("  No pagination found")
                    has_more_pages = False
                
                page += 1
                
            except TimeoutException:
                print(f"  Timeout on page {page}")
                has_more_pages = False
            except Exception as e:
                print(f"  Error on page {page}: {e}")
                has_more_pages = False
        
    finally:
        driver.quit()
        print("\nBrowser closed")
    
    df = pd.DataFrame(all_data)
    return df


def save_results(df, search_location, output_file=None):
    """Save scraped data to CSV file"""
    if output_file is None:
        safe_location = search_location.replace(' ', '_').replace(',', '')
        output_file = f'omara_agents_{safe_location}.csv'
    
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\nData saved to {output_file}")
    print(f"Total records scraped: {len(df)}")


def main():
    search_location = "Melbourne"
    
    print("Starting OMARA register scrape with Selenium...")
    print("=" * 50)
    print("\nNOTE: This script requires Chrome and ChromeDriver to be installed")
    print("Install with: pip install selenium")
    print("Download ChromeDriver from: https://chromedriver.chromium.org/")
    print("=" * 50)
    
    # Scrape the data
    df = scrape_omara_with_selenium(search_location=search_location, max_pages=50)
    
    # Display summary
    print("\n" + "=" * 50)
    print(f"Scraping complete!")
    print(f"Total agents found in {search_location}: {len(df)}")
    
    if len(df) > 0:
        print("\nSample data (first 5 records):")
        print(df.head())
        
        print("\nBreakdown by state:")
        print(df['state'].value_counts())
        
        print("\nBreakdown by suburb:")
        print(df['suburb'].value_counts().head(10))
        
        # Save to CSV
        save_results(df, search_location)
    else:
        print("\nNo data was scraped.")
        print("Possible issues:")
        print("1. ChromeDriver not installed or not in PATH")
        print("2. Location search returned no results")
        print("3. Website structure has changed")


if __name__ == "__main__":
    main()