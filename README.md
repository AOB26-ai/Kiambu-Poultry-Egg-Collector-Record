# Poultry Egg Production API

A simple REST API for logging daily egg production per shed. Built for a poultry farmer in Kiambu who currently tracks production via WhatsApp and wants a cleaner way to record and total eggs at the end of the week.

## Features

- **POST `/api/eggs`** – Log a daily egg record (shed name, date, count)
- **GET `/api/eggs`** – Retrieve all records with a running total
- In-memory storage (data resets when the server restarts)

## Requirements

- Python 3.8+
- Flask

## Installation

```bash
pip install flask

## Pricing & Monetization Model (Kiambu Poultry Farm)

### One-Time Build & Deployment Fee: KES 25,000 – KES 35,000
* **What it covers:**
  * Backend REST API with persistent database storage (SQLite/PostgreSQL so records survive server restarts) and API key protection.
  * Simple mobile-friendly web form or WhatsApp webhook integration so farmhands can log daily tray/egg counts from their phones in seconds.
  * Weekly summary view broken down by shed and total farm output.
  * Cloud deployment, custom domain/SSL setup, and hands-on training for the farmer and shed attendants.

## OUTPUT
### You send 
{
  "shed": "Shed A",
  "date": "2026-11-17",
  "count": 120
}

### The API replies
{
  "message": "Record logged successfully",
  "record": {
    "shed": "Shed A",
    "date": "2026-11-17",
    "count": 120
  }
}

## When you check everything the API replies with all the total + the records.
{
  "records": [
    { "shed": "Shed A", "date": "2026-11-17", "count": 120 },
    { "shed": "Shed A", "date": "2026-11-18", "count": 135 },
    { "shed": "Shed B", "date": "2026-11-17", "count": 98 },
    { "shed": "Shed B", "date": "2026-11-18", "count": 110 }
  ],
  "running_total": 463
}

### Monthly Maintenance & Hosting Retainer: KES 3,000 – KES 5,000 / month
* **What it covers:**
  * Cloud server and database hosting uptime monitoring.
  * Automated weekly data backups (preventing loss of historical production records).
  * Minor feature adjustments (e.g., adding a 4th shed, tracking feed consumption, or exporting Saturday reports to CSV/PDF) and WhatsApp/phone support.
