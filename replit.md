# 2Captcha Multi-Balance Checker

## Overview

This is a Flask-based web application that allows users to check the balance of multiple 2Captcha API keys simultaneously. The application provides a simple web interface where users can input multiple API keys (one per line) and retrieve their current balances from the 2Captcha service.

The project consists of:
- A Flask web server that serves the frontend and handles API requests
- A simple HTML/JavaScript frontend using Tailwind CSS for styling
- A standalone Python script for checking a single API key balance via environment variable

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python) - Chosen for its simplicity and lightweight nature, ideal for a single-purpose utility application
- **CORS**: Enabled via flask-cors to allow cross-origin requests if needed
- **API Pattern**: Single POST endpoint (`/check-balances`) that accepts an array of API keys and returns balance information for each

### Frontend Architecture
- **Rendering**: Server-side rendered HTML template (Jinja2)
- **Styling**: Tailwind CSS via CDN - eliminates need for build tooling
- **Icons**: Font Awesome via CDN
- **JavaScript**: Vanilla JS for API calls and DOM manipulation (inline in template)

### Request Flow
1. User enters API keys in textarea (one per line)
2. Frontend sends POST request to `/check-balances` with array of keys
3. Backend iterates through keys, calling 2Captcha API for each
4. Results are aggregated and returned as JSON
5. Frontend displays success/error status for each key

### Security Considerations
- API keys are partially masked in responses (showing only first 4 and last 4 characters)
- Keys are processed server-side to avoid exposing them in browser network logs to third parties
- Request timeout of 10 seconds prevents hanging on slow responses

## External Dependencies

### Third-Party APIs
- **2Captcha API**: `https://api.2captcha.com/getBalance` - Used to retrieve account balance for given API keys. Requires valid 2Captcha API key(s) from user.

### Python Dependencies
- `flask` - Web framework
- `flask-cors` - CORS support for Flask
- `requests` - HTTP client for calling 2Captcha API

### CDN Resources
- Tailwind CSS (styling)
- Font Awesome (icons)
- Google Fonts (Inter font family)

### Environment Variables
- `TWO_CAPTCHA_API_KEY` (optional) - Used only by the standalone `check_balance.py` script for single-key checking