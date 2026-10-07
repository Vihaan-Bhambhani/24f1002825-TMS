# Trekking Management Application

A compact role-based trekking management web application built with **Python, Flask, SQLAlchemy, SQLite, Jinja2, and Bootstrap 5**.

The system supports three roles:

- **Admin** — manages treks, staff, users, approvals, and bookings
- **Trek Staff** — manages assigned treks and participants
- **Trekker** — browses available treks and manages bookings

## What it demonstrates

- Session-based authentication and role-based access control
- Flask Application Factory and Blueprint architecture
- SQLAlchemy relational modelling
- Trek CRUD and staff assignment
- Staff approval and blacklist workflows
- Trek availability and slot management
- Booking/cancellation business rules
- Ownership checks for user and staff resources
- Search, pagination, and role-specific dashboards

## Core workflow

```text
Admin
 ├── Approves staff
 ├── Creates/manages treks
 └── Assigns staff
          │
          ▼
     Trek Staff
          │
          ▼
     Trek Management
          │
          ▼
       Trekkers
          │
          ▼
   Booking / Cancellation
```

## Database design

The application uses four core entities:

| Entity | Purpose |
|---|---|
| User | Authentication, roles, account state |
| StaffProfile | Staff-specific profile and approval information |
| Trek | Trek listings, schedules, capacity, and assignment |
| Booking | Trekker bookings and booking status |

The relational model connects users to staff profiles and bookings, staff to assigned treks, and treks to bookings.

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ORM | Flask-SQLAlchemy / SQLAlchemy |
| Database | SQLite |
| Templates | Jinja2 |
| Frontend | Bootstrap 5, custom CSS |
| Authentication | Flask sessions + Werkzeug password hashing |

## Run locally

```bash
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Configure an initial admin password with:

```text
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=choose-a-strong-password
```

Then run:

```bash
python app.py
```

The SQLite database and initial admin account are created automatically on first run.

## Project structure

```text
├── app.py
├── config.py
├── extensions.py
├── models.py
├── seed.py
├── routes/
│   ├── auth.py
│   ├── admin.py
│   ├── staff.py
│   └── user.py
├── templates/
└── static/
```

## Notes

This is a supporting application project demonstrating Python backend development, relational data modelling, authentication, and business-rule implementation. It is intentionally kept lightweight rather than positioned as a production trekking platform.

---
**Author:** Vihaan Bhambhani
