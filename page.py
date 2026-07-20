from quart import Quart, render_template_string

app = Quart(__name__)

# Basic HTML template for the home page keeping the same layout base
HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bot Status</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background-color: #1e293b;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }
        .status-dot {
            height: 12px;
            width: 12px;
            background-color: #22c55e;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }
        h1 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        p {
            color: #94a3b8;
            font-size: 0.95rem;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1><span class="status-dot"></span>Bot Server Active</h1>
        <p>The application service is running normally.</p>
    </div>
</body>
</html>
"""

@app.route('/')
async def home():
    """Serves the main landing page."""
    return await render_template_string(HOME_HTML)

@app.route('/health')
async def health():
    """Simple ping route for UptimeRobot / Render keep-alive."""
    return "OK", 200
