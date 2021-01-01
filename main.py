
import os
from src.api import Api

port = int(os.environ.get("PORT", 5000))


# Run the app
if __name__ == '__main__':
    Api().run('0.0.0.0', port=port)
