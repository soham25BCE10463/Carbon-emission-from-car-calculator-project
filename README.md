# Carbon Emission from Car Calculator Project 

##  Project Overview
The **Carbon Emission from Car Calculator** is a Python-based command-line project designed to estimate the carbon emission of vehicle travel. By analyzing fuel type (Petrol/Diesel), distance traveled, and fuel efficiency, the tool calculates total CO2 emissions using standard stoichiometric factors.

This project was developed by me as part of the **Python Essentials** course evaluation.It demonstrates **Modular Programming** by splitting logic, user interface, and configuration into separate files.

##  Features
- **Modular Architecture:** The codebase is split into 6 specific modules (`logic`, `ui`, `inputs`, etc.) for maintainability and easy reading
- **Dual Fuel Support:** Accurate emission factors for **Petrol** (2.31 kg/L) and **Diesel** (2.68 kg/L).
- **Eco-Feedback System:** Provides immediate feedback (e.g., "Plant some trees!") based on the severity of emissions.
- **Robust Error Handling:** safely manages non-numeric inputs and prevents application crashes.

##  Technologies Used
- **Language:** Python 3.x
- **Libraries:** Standard Python libraries (`sys` for system exit operations).
- **Tools:** GitHub for version control.

##  Project Structure
The source code is organized into a `src` package containing **6 meaningful modules**

```text
Carbon-emission-from-car-calculator-project/
│
├── src/
│   ├── main.py           # Entry point: Orchestrates the application flow
│   ├── config.py         # Configuration: Stores constants and emission factors
│   ├── logic.py          # Business Logic: Performs the math calculations
│   ├── inputs.py         # Input Module: Handles user input & validation
│   ├── ui.py             # User Interface: Handles all print statements/banners
│   ├── utils.py          # Utilities: Helper functions (formatting lines)
│   └── __init__.py       # Package initializer
│
├── screenshots/
│   ├── output.png        # Main execution result
│   ├── step1.png         # Input demonstration
│   ├── step2.png         # Calculation demonstration
│   └── step3.png         # Error handling demonstration
│
├── statement.md          # Problem statement and scope definition
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (Standard Python)
```
