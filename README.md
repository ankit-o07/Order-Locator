# 🗺️ Order Locator - FastAPI + MongoDB + Google Maps

This project is a simple FastAPI web application that collects order details through a form and displays the location on Google Maps based on the given address.

---

## 🚀 Features

- Collects Name, Phone Number, Address, and Preferred Delivery Time
- Saves the order in MongoDB
- Displays the address location using Google Maps
- Clean HTML frontend using Jinja2 templates

---

## 🧰 Tech Stack

- FastAPI
- MongoDB (via PyMongo)
- Google Maps JavaScript & Geocoding API
- Jinja2 Templating
- Python Dotenv

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/order-locator.git
cd order-locator
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:

```env
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
```

### 5. Start MongoDB
Make sure MongoDB is running locally at `mongodb://localhost:27017`

### 6. Run the App
```bash
uvicorn main:app --reload
```

Then go to: [http://localhost:8000](http://localhost:8000)

---

## 🌍 Google Maps API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project
3. Enable these APIs:
   - Maps JavaScript API
   - Geocoding API
4. Create credentials → API Key
5. Paste it into your `.env` file

---

## 📁 Project Structure

```
order-locator/
├── main.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── templates/
│   ├── form.html
│   └── map.html
└── static/
    └── (optional CSS or assets)
```

---

## 🧑‍💻 Author

**Your Name**  
📧 your@email.com  
🌐 [your-portfolio.com](https://your-portfolio.com)

---

## 📄 License

This project is licensed under the MIT License.