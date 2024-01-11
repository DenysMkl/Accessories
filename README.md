## Accessories API
### Description 
This project is a Python-based web scraping tool that extracts data about accessories for laptops from a target website and provide API for access to data from storage.
1. Web Scraping: Utilizes Python for web scraping, extracting data from a specified website
2. FastAPI framework: Provides API service to offer choices for accessories that will combined with specific laptop.
3. MongoDB Integration: Stores the extracted data in MongoDB, allowing for efficient data retrieval and management

### Prerequisites
1. Python 3.9+
2. MongoDB
3. Docker

### Run
* git clone https://github.com/DenysMkl/Accessories.git

### Setup workplace
1. Install virtual environment (not required)
   * On Linux/MacOS
     ```
     make create-venv
     ```
   * On Windows
     ```
     python -m venv venv
     ```
2. Activate virtual environment
   * On Linux/MacOS
     ```
     source venv/bin/activate
     ```
   * On Windows
     ```
     .\venv\Scripts\activate
     ```
3. Install the dependencies
   * On Linux/MacOS
     ```
     make start-dev
     ```
   * On Windows
     ```
     pip install -r requirements.txt
     ```

### Usage
  1. Run `make build` which will create all neccessary images for Docker.
  2. Run `make run` which will create and start docker containers.
     + my_con - run FastAPI server;
     + mongodb - run MongoDB database;
     + parse - run python script to parse data about accessories.
