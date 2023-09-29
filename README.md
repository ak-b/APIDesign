# API Design

# Simple RESTful API Design with Flask

This repo provides a basic example of designing a RESTful API using Flask.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ak-b/flask-api-design.git

2. Create a virtual environment and activate it:
cd flask-api-design
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the dependencies:
pip install -r requirements.txt

4.Run the app:
python app.py

## API Routes
GET /items: Fetch all items.
POST /items: Create a new item.
GET /items/<int:id>: Fetch a specific item by ID.
PUT /items/<int:id>: Update a specific item by ID.
DELETE /items/<int:id>: Delete a specific item by ID.
