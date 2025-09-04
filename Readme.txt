Little Lemon Restaurant API Endpoints

Base URL (local): http://127.0.0.1:8000/

Restaurant app
- GET    /restaurant/menu/                 - List menu items.
- POST   /restaurant/menu/                 - Create a menu item.
- GET    /restaurant/menu/<id>             - Retrieve a menu item.
- PUT    /restaurant/menu/<id>             - Replace a menu item.
- PATCH  /restaurant/menu/<id>             - Update a menu item.
- DELETE /restaurant/menu/<id>             - Delete a menu item.

Bookings (router)
- GET    /tables/                          - List bookings.
- POST   /tables/                          - Create a booking.
- GET    /tables/<id>/                     - Retrieve a booking.
- PUT    /tables/<id>/                     - Replace a booking.
- PATCH  /tables/<id>/                     - Update a booking.
- DELETE /tables/<id>/                     - Delete a booking.

Authentication (Djoser + DRF Token)
- POST   /restaurant/api-token-auth        - Obtain DRF auth token (username, password).
- GET    /auth/users/                      - List users (auth required depending settings).
- POST   /auth/users/                      - Create user (register).
- GET    /auth/users/me/                   - Current user profile.
- POST   /auth/token/login/                - Obtain token via Djoser (username, password).
- POST   /auth/token/logout/               - Revoke token.

Notes
- Include Authorization: Token <your_token> header for protected endpoints.
- Content-Type: application/json for POST/PUT/PATCH bodies.
