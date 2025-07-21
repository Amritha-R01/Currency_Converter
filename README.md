💱 Currency Converter CLI Tool (Python)

This command-line tool converts currencies using real-time exchange rates from ExchangeRate-API.

📦 Setup Instructions:

1. Install required libraries:
   pip install requests python-dotenv

2. Create a `.env` file in this folder with the following content:
   API_KEY=your_api_key_here

   Replace `your_api_key_here` with your own key from https://www.exchangerate-api.com/

3. Run the program:
   python currency_converter.py

💾 Optional:
Conversion history is saved to `conversion_history.txt` if you choose to save it after a conversion.

📌 Note:
This project does not include the `.env` file for security reasons. Please create your own.
