Perfect 👍 — here’s a **complete, professional `README.md`** for your GitHub repository.
It explains everything: Scrapy, MongoDB Atlas, dataset handling, setup steps, and license — all in clean Markdown format.

---

## 🏠 Zameen.com Real Estate Data Scraper

This project is a **Scrapy-based web scraping tool** designed to extract detailed property listings from **[Zameen.com](https://www.zameen.com)** — Pakistan’s largest real estate platform.
It collects valuable data such as **title, location, price, beds, baths, area, coordinates, agent details**, and more.
The scraped data is stored in **MongoDB Atlas** and exported as a dataset (`zameen_updated_property_dataset.zip`).

---

### 📋 Features

* 🔍 Scrapes listings from **Zameen.com** for multiple cities and property types.
* 🧩 Extracts both **visible and hidden fields** (from embedded JSON in `window.state`).
* 💾 Saves data to **MongoDB Atlas** (cloud database).
* 📁 Automatically exports data to a **CSV dataset** (`zameen_updated_property_dataset.zip`).
* 🚀 Supports large-scale scraping with **pagination**, **custom headers**, and **concurrency controls**.
* 🔐 Avoids detection using random User-Agent and delay throttling.

---

### 🧠 Tech Stack

| Component       | Technology                                                    |
| --------------- | ------------------------------------------------------------- |
| **Framework**   | Scrapy                                                        |
| **Language**    | Python 3.10+                                                  |
| **Database**    | MongoDB Atlas                                                 |
| **Data Format** | JSON / CSV                                                    |
| **Deployment**  | GitHub + Local Scrapy Runner                                  |
| **Dataset**     | `zameen_updated_property_dataset.zip` (contains `zameen.csv`) |

---

### 🗂️ Folder Structure

zameen-realestate-scrapy-project/
│
├── zameendata/
│   ├── zameendata/                      # Main Scrapy package
│   │   ├── spiders/                     # Spider folder
│   │   │   ├── __pycache__/             # Cache files
│   │   │   └── mongoscraper.py          # Main Zameen.com spider
│   │   │
│   │   ├── __init__.py                  # Package initializer
│   │   ├── items.py                     # Defines data model for scraped fields
│   │   ├── middlewares.py               # Optional Scrapy middlewares
│   │   ├── pipelines.py                 # MongoDB Atlas pipeline (data storage)
│   │   ├── settings.py                  # Scrapy configuration and performance tuning
│   │   └── __pycache__/                 # Python cache folder
│
├── scrapy.cfg                           # Scrapy project configuration file
├── LICENSE                              # MIT License for open-source use
├── README.md                            # Full project documentation
└── zameen_updated_property_dataset.zip  # Final dataset (CSV file inside)


### 🧩 Scraped Fields

| Field                | Description                             |
| -------------------- | --------------------------------------- |
| Title                | Property headline                       |
| Location             | Full address/location                   |
| Price                | Listed price                            |
| Beds                 | Number of bedrooms                      |
| Baths                | Number of bathrooms                     |
| Area                 | Covered area (sq ft / sq yd)            |
| Details_URL          | Link to full property page              |
| Property_ID          | Unique property identifier              |
| City                 | Property city                           |
| Province             | Province name                           |
| Type                 | Property type (House, Plot, Flat, etc.) |
| Purpose              | Buy or Rent                             |
| Latitude & Longitude | Coordinates for mapping                 |
| Contact_Name         | Agent name                              |
| Agency_Name          | Agency company                          |
| Mobile_Number        | Agent contact number                    |

---

### ⚙️ Setup Instructions

#### 1. Clone this repository

```bash
git clone https://github.com/zaifi320/zameen-realestate-scrapy-project.git
cd zameendata
```

#### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Add your MongoDB Atlas credentials

In `pipelines.py`, add your MongoDB Atlas URI and database name:

```python
self.client = pymongo.MongoClient("your_mongodb_atlas_connection_string")
self.db = self.client["zameen_database"]
```

#### 5. Run the spider

```bash
scrapy crawl zameen1 -o zameen.csv
```

This will:

* Scrape property listings
* Insert data into MongoDB Atlas
* Export results into `zameen.csv`
* (You can find this file compressed as `zameen_updated_property_dataset.zip`)

---

### 📊 Dataset

The full dataset of scraped listings is available in this repository as:

📁 **`zameen_updated_property_dataset.zip`**
It contains a **CSV file (`zameen.csv`)** with all extracted property data.

If the dataset is too large for GitHub upload, it can alternatively be hosted on Google Drive or Kaggle, with a link provided here.

---

### 🚀 Performance Optimizations

The scraper uses:

* `DOWNLOAD_DELAY = 0.05`
* `AUTOTHROTTLE_ENABLED = True`
* `CONCURRENT_REQUESTS = 32`
* `AUTOTHROTTLE_TARGET_CONCURRENCY = 8`

These settings allow **fast yet safe scraping** without overwhelming Zameen servers.

---

### 🧰 Dependencies

```
scrapy
pymongo
requests
beautifulsoup4
```

---

### 🧑‍💻 Author

**Huzaifa Bin Saeed**
📍 Pakistan
💼 Final Year Project – Real Estate Data Collection and Analytics
📧 Contact: [Your Email or GitHub Profile Link]

---

### 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Huzaifa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...
```

---

Would you like me to include a **Google Drive link placeholder** (like `[Download Dataset]()`), or are you uploading the `.zip` directly into the repository using **Git LFS**?
I can edit the README accordingly.
