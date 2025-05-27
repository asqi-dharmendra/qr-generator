# QR Code Generator Web Application

This project is a simple web application that generates QR codes based on user input. It is built using Flask, a lightweight web framework for Python.

## Project Structure

```
qr-generator
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── qr_generator.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   └── templates
│       ├── base.html
│       └── index.html
├── main.py
├── config.py
├── requirements.txt
├── Procfile
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd qr-generator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Deployment

To deploy the application, you can use platforms like Heroku. Make sure to include the `Procfile` for deployment instructions.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.