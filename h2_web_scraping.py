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

            # Example: Extract all <h2> headings (You can modify this based on your needs)
            headings = soup.find_all('h2')

            if not headings:
                text_area.insert(tk.INSERT, "No <h2> tags found on the page\n")
                return
            
            # Prepare the text to display
            display_text = ""
            for i, heading in enumerate(headings, 1):
                display_text += f"{i}. {heading.text.strip()}\n"

            # Insert the scraped data into the text widget
            text_area.delete(1.0, tk.END)  # Clear the text area
            text_area.insert(tk.INSERT, display_text)  # Insert the new data
        else:
            text_area.insert(tk.INSERT, f"Failed to retrieve the webpage. Status code: {response.status_code}\n")
    
    except Exception as e:
        text_area.insert(tk.INSERT, f"Error occurred: {e}\n")  # Display any error

# Create the GUI window
window = tk.Tk()
window.title("Web Scraper GUI")
window.geometry("600x400")

# Create a label
label = tk.Label(window, text="Web Scraper", font=("Arial", 14))
label.pack(pady=10)

# Create a scrolled text area to display the scraped data
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=15, font=("Arial", 12))
text_area.pack(pady=10)

# Create a button to trigger the web scraping function
scrape_button = tk.Button(window, text="Scrape Website", command=scrape_website, font=("Arial", 12))
scrape_button.pack(pady=10)

# Run the GUI loop
window.mainloop()   