# 🧮 Zubair Calculator

A desktop calculator built with Python and Tkinter, featuring a modern dark interface, basic arithmetic operations, and a scientific calculator mode.

## ✨ Features

### Basic Calculator

* Addition, subtraction, multiplication, and division
* Percentage calculations
* Decimal number support
* Clear and backspace buttons
* Keyboard input support

### Scientific Calculator

* Square and cube operations
* Exponentiation
* Square root and cube root operations
* Sine, cosine, and tangent functions
* Base-10 logarithms
* Factorial calculations
* Parentheses for mathematical expressions

### User Interface

* Dark-themed interface
* Orange operation buttons
* Separate basic and scientific calculator modes
* Error messages for invalid mathematical expressions

## 🛠️ Technologies Used

* **Python** — Application logic and mathematical operations
* **Tkinter** — Graphical user interface
* **Math** — Mathematical functions

## 📁 Project Structure

```text
zubair-calculator/
├── zubair_calculator.py
├── README.md
└── .gitignore
```

## ⚙️ Requirements

* Python 3
* Tkinter support in your Python installation

No third-party Python packages are required by the current implementation.

## 🚀 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/zubair-calculator.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd zubair-calculator
```

### 3. Run the Calculator

```bash
python zubair_calculator.py
```

On some systems, you may need to use:

```bash
python3 zubair_calculator.py
```

The calculator window should open on your desktop.

## ⌨️ Keyboard Controls

* **Numbers:** Enter numerical values.
* **Arithmetic operators:** Enter `+`, `-`, `*`, or `/`.
* **Enter:** Evaluate the expression.
* **Backspace:** Delete the last character.

## 📐 Scientific Functions

| Function | Operation                 |
| -------- | ------------------------- |
| `x²`     | Square                    |
| `x³`     | Cube                      |
| `x^y`    | Raise a number to a power |
| `√x`     | Square root               |
| `∛x`     | Cube root                 |
| `sin`    | Sine in degrees           |
| `cos`    | Cosine in degrees         |
| `tan`    | Tangent in degrees        |
| `log`    | Base-10 logarithm         |
| `!`      | Factorial                 |

## ⚠️ Limitations

* The current implementation evaluates expressions using Python's `eval()` function. Although the application restricts built-in access, it should be replaced with a safer mathematical expression parser before accepting untrusted input.
* The calculator does not currently provide calculation history.
* Mathematical domain errors, such as taking the logarithm of a negative number, produce an error message.
* Percentage behavior is simplified and may differ from that of commercial calculators.
* Scientific operations use expression-string manipulation rather than a dedicated mathematical expression parser.

## 👨‍💻 Author

**Mohammad Zubair Safi**

Software Engineering Student | Web Developer

## 📄 License

No license has been selected for this project yet. Please contact the author for permission before redistributing or reusing the code.
