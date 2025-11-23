# Carbon Emission from Car Calculator Project 

##  Project Overview
The **Carbon Emission from Car Calculator** is a Python-based command-line project designed to estimate the carbon emission of vehicle travel. By analyzing fuel type (Petrol/Diesel), distance traveled, and fuel efficiency, the tool calculates total Carbon emissions from car using standard stoichiometric factors.

This project is developed by me as part of the **Python Essentials** course evaluation for vityarthi.It demonstrates **Modular Programming** by splitting logic, user interface, and configuration into separate files.

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
## Steps to Install & Run
1. Clone the repository:
  ``` git clone [INSERT YOUR REPO LINK HERE]```
2. Navigate to the Source Directory:
  ``` cd src```
3. Run the Application:
  ``` python main.py```
## Instructions for Testing
To verify the application works as expected, perform the following test case:
 example 1: Standard Petrol Trip
  -Input: Fuel = 1 (Petrol), Distance = 1000, Mileage = 18
  -Expected Output: Total Emission ~ 128.33 kg. Message: "YOUR CAR IS POLLUTING THE ENVIRONMENT PLEASE PLANT SOME TREES".

  ##  Screenshots
  ***step 1***
  ![step 1](screenshots/step1.png)

***step 2***
![step 2](screenshots/step2.png)

***step 3***
![step 3](screenshots/step3.png)

***final out put***
![output](screenshots/output.png)


  ##  Author
  **Name** - SOHAM SUDARSHAN SHINDE
  **REG No** - 25BCE10463
  **Course name** - Python essentials

