# Post Office Management API

A production-level REST API for managing Indian Post Office operations, built with Django REST Framework. Designed by an active ABPM (Assistant Branch Post Master) based on real daily post office workflows.

🔗 **Live API:** https://post-office-mgmt-api.onrender.com
📁 **GitHub:** https://github.com/Sudipta7-ops/post-office-mgmt-api

> Note: First request may take 30-50 seconds on free tier (cold start)

---

## What This Project Does

This API digitizes the core operations of an Indian branch post office:
- Staff login with government employee ID
- Speed post article booking and tracking
- Mail bag receive, scan, delivery, and dispatch workflow
- Role based access for different staff levels

---

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.12 | Core language |
| Django 6.0 | Web framework |
| Django REST Framework | API layer |
| PostgreSQL | Production database |
| JWT (SimpleJWT) | Authentication |
| GitHub Actions | CI/CD pipeline |
| Render | Cloud deployment |

---

## Features

- **JWT Authentication** — Login with employee ID, access + refresh tokens
- **Custom User Model** — Employee ID as login field instead of username
- **Role Based Permissions** — ABPM, BPM, Admin with different access levels
- **Article Number Validation** — Enforces format like `EE123456789IN`
- **Search & Filter** — Search bookings by article number
- **Ordering & Pagination** — Sort by date/weight, 10 results per page
- **Custom Exception Handling** — Consistent JSON error responses
- **API Versioning** — All endpoints under `/api/v1/`
- **Throttling** — 1000 requests/day per user
- **Signals** — Auto logs every new booking
- **Unit Tests** — 5 tests, all passing
- **CI/CD** — GitHub Actions runs tests on every push

---

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/token/` | Login with employee ID + password |
| POST | `/api/v1/token/refresh/` | Get new access token |

### Booking
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/bookings/` | List all bookings |
| POST | `/api/v1/bookings/` | Create new speed post booking |
| GET | `/api/v1/bookings/{article_number}/` | Get single booking |
| PATCH | `/api/v1/bookings/{article_number}/` | Update booking |
| DELETE | `/api/v1/bookings/{article_number}/` | Delete booking (Admin only) |

### Delivery
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/bags/` | Receive mail bag from account office |
| GET | `/api/v1/bags/` | List all bags |
| GET | `/api/v1/bags/{bag_code}/` | Get bag with all articles |
| POST | `/api/v1/bags/{bag_code}/scan/` | Scan article into bag |
| PATCH | `/api/v1/articles/{id}/invoice/` | Mark article as delivered/undelivered |
| PATCH | `/api/v1/bags/{bag_code}/dispatch/` | Dispatch bag to account office |

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/Sudipta7-ops/post-office-mgmt-api.git
cd post-office-mgmt-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env  # Edit with your values

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

---

## Environment Variables

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:password@host/dbname
```

---

## Running Tests

```bash
python manage.py test booking
```

CI/CD: Tests run automatically on every push via GitHub Actions.

---

## Project Structure
post_office_mgmt/
├── accounts/           # Custom user model, employee ID login
├── booking/            # Speed post booking CRUD + validation
│   ├── models.py
│   ├── serializers.py  # Article number format validation
│   ├── views.py        # List, create, retrieve, update, delete
│   ├── permissions.py  # IsABPM, IsBPM, IsAdmin
│   ├── signals.py      # Auto log on booking creation
│   └── tests.py        # 5 unit tests
├── delivery/           # Mail delivery workflow
│   ├── models.py       # Bag, DeliveryArticle models
│   ├── views.py        # Receive, scan, invoice, dispatch
│   └── serializers.py
├── postal/             # Project config
│   ├── settings.py
│   ├── urls.py
│   └── exceptions.py   # Custom JSON error handler
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI pipeline
├── build.sh            # Render build script
└── requirements.txt
---

## Real World Context

This project is built on actual post office operations. The booking module maps directly to the speed post booking portal used in Indian branch post offices. The delivery module replicates the physical mail bag workflow — receiving from account office, scanning articles, delivery boy dispatch, invoicing, and returning the bag.

---

## Author

**Sudipta Barik**  
Assistant Branch Post Master, India Post  
GitHub: [@Sudipta7-ops](https://github.com/Sudipta7-ops)