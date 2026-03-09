# app.py – Day 2: Added /tickets route 
# Simulates a backend API returning an L2 ticket queue

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# The home page route ('/')
@app.route('/')
def home():
    # Returning basic HTML with a clickable link to our new route
    return """
    <h1>Enterprise Customer Support Ticket System</h1>
    <p>Status: Day 2 - Active</p>
    <p><a href="/tickets">View Open L2 Tickets</a></p>
    """

# The new tickets route ('/tickets')
@app.route('/tickets')
def tickets():
    # 1. LISTS & DICTIONARIES: This simulates a database response or API payload
    mock_tickets = [
        {"id": 101, "issue": "Device enrollment failed", "status": "Open", "client": "Telecom A"},
        {"id": 102, "issue": "FER request: Add Android 16 support", "status": "In Progress", "client": "Gov Dept"},
        {"id": 103, "issue": "API integration timeout", "status": "New", "client": "Bank B"}
    ]
    
    # Start building our HTML string
    html = "<h2>Open L2 Support Tickets</h2><ul>"
    
    # 2. FOR LOOP: Iterate through each dictionary inside our list
    for ticket in mock_tickets:
        
        # 3. F-STRING: Inject the dictionary values into the HTML bullet points
        html += f"<li><strong>ID {ticket['id']}</strong>: {ticket['issue']} | Status: {ticket['status']} | Client: {ticket['client']}</li>"
        
    # Close the HTML list and add a back button
    html += "</ul><br><a href='/'>Go Back</a>"
    
    return html

# Start the server with debugging turned on
if __name__ == '__main__':
    app.run(debug=True)