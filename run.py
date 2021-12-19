from app import app
from db import db

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True, host="0.0.0.0", port=80)