# app.py – Day 1: Basic Customer Support Portal (March 7, 2026)
# This creates a simple web server using Flask – like the homepage of our ticket system

from flask import Flask  # Import Flask to build the web app

app = Flask(__name__)    # Create the main app object

# Define the home route: when someone visits "/", show this page
@app.route('/')
def home():
    return """
    <h1>Hello from Ashish's Customer Support Ticket System!</h1>
    <p>Date: March 7, 2026 – Day 1 of AWS + Python learning</p>
    <p>This is a local web app running in venv. Soon we'll connect it to AWS RDS!</p>
    <p>Mirrors my Samsung work: L2 tickets, FER registration, customer onboarding.</p>
    """  
    # ↑ Feel free to edit the text/HTML here – it's what shows in your browser

# This block runs the server only if we execute this file directly
if __name__ == '__main__':
    app.run(debug=True)  
    # debug=True: shows detailed errors + auto-reloads when you save changes