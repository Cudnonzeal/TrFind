 Step 1: Get the HTML
    url = input("Enter the URL to scrape: ").strip()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    clean_text = soup.get_text(separator="\n", strip=True)
    # Step 2: Extract data
    with open("page.html", "w", encoding="utf-8") as f:
        f.write(str(clean_text))
