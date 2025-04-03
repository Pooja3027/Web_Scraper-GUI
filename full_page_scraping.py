import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext

# Function to scrape the website and display data in the GUI
def scrape_website():
    url = "https://en.wikipedia.org/wiki/Cloud_computing"  # Replace with your URL
    
    # Display status in the GUI that scraping is in progress
    text_area.delete(1.0, tk.END)  # Clear the text area
    text_area.insert(tk.INSERT, "Scraping in progress...\n")

    try:
        # Send a GET request to the website
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all headings, paragraphs, and links
            content = []

            # Extract headings (h1 to h6)
            for i in range(1, 7):  
                for heading in soup.find_all(f'h{i}'):
                    content.append(f"{heading.name.upper()}: {heading.text.strip()}")

            # Extract all paragraphs
            for paragraph in soup.find_all('p'):
                content.append(f"Paragraph: {paragraph.text.strip()}")

            # Extract all links
            for link in soup.find_all('a', href=True):
                content.append(f"Link: {link.text.strip()} -> {link['href']}")

            # Extract unordered and ordered lists
            for ul in soup.find_all('ul'):
                for li in ul.find_all('li'):
                    content.append(f"List Item: {li.text.strip()}")

            for ol in soup.find_all('ol'):
                for li in ol.find_all('li'):
                    content.append(f"Ordered List Item: {li.text.strip()}")

            # Insert the scraped data into the text widget
            text_area.delete(1.0, tk.END)  # Clear the text area
            text_area.insert(tk.INSERT, "\n".join(content))  # Insert the new data

        else:
            text_area.insert(tk.INSERT, f"Failed to retrieve the webpage. Status code: {response.status_code}\n")
    
    except Exception as e:
        text_area.insert(tk.INSERT, f"Error occurred: {e}\n")  # Display any error

# Create the GUI window
window = tk.Tk()
window.title("Advanced Web Scraper GUI")
window.geometry("700x500")

# Create a label
label = tk.Label(window, text="Web Scraper - Full Page Details", font=("Arial", 14))
label.pack(pady=10)

# Create a scrolled text area to display the scraped data
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=20, font=("Arial", 10))
text_area.pack(pady=10)

# Create a button to trigger the web scraping function
scrape_button = tk.Button(window, text="Scrape Website", command=scrape_website, font=("Arial", 12))
scrape_button.pack(pady=10)

# Run the GUI loop
window.mainloop()
