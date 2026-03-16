# Simple Password Generator

A lightweight Python utility designed to generate high-entropy, customisable passwords with a real-time security strength evaluator.

---

## Key Features
* **Customisation:** Toggle numbers and special characters on/off.
* **Dynamic Entropy:** Specify any length (upto 20 characters) to meet specific site requirements.
* **Live Strength Gauge:** Instant feedback using a multi-factor scoring algorithm.
* **Bulletproof Logic:** Includes try-except blocks to handle invalid user inputs gracefully.

## How the Strength Gauge Works
The app evaluates the password based on a 5-point scoring system:

- **Length (Basic):** +1 point if 8+ characters
- **Length (Advanced):** +1 point if 12+ characters
- **Mixed Case:** +1 point for using both UPPER and lower case
- **Numbers:** +1 point for including 0-9
- **Symbols:** +1 point for including !@#$%^&*
  
## Installation & Usage
1. Clone the repository to your local machine.
2. Navigate to the project folder in your terminal.
3. Run the application using the command:
   `python password-generator-v1.0.py`
