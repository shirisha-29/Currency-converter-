import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox

class CurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Currency Converter")
        self.setGeometry(100, 100, 400, 200)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add input label and text box
        self.input_label = QLabel("Enter amount:")
        layout.addWidget(self.input_label)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("e.g., 83")
        layout.addWidget(self.amount_input)

        # Currency selection dropdowns
        self.from_currency = QComboBox()
        self.from_currency.addItems(["United States(USD)", "Europe(EUR)", "India(INR)"])
        layout.addWidget(self.from_currency)

        self.to_currency = QComboBox()
        self.to_currency.addItems(["United States(USD)", "Europe(EUR)", "India(INR)"])
        layout.addWidget(self.to_currency)

        # Adding button to calculate
        self.convert_button = QPushButton("Convert the currency")
        self.convert_button.clicked.connect(self.convert_currency)
        layout.addWidget(self.convert_button)

        # Adding output label
        self.output_label = QLabel("")
        layout.addWidget(self.output_label)

        # Exchange rates 
        self.exchange_rates = {
            "United States(USD)": {"Europe(EUR)": 0.93, "India(INR)": 85.67, "United States": 1.0},
            "Europe(EUR)": {"United States(USD)": 1.08, "India(INR)": 92.58, "Europe(EUR)": 1.0},
            "India(INR)": {"United States(USD)": 0.012, "Europe(EUR)": 0.011, "India(INR)": 1.0}
        }

    def convert_currency(self):
        """Converts currency based on the selected exchange rate."""
        try:
            amount = float(self.amount_input.text())
            from_curr = self.from_currency.currentText()
            to_curr = self.to_currency.currentText()

            # Converting using exchange rates
            converted_amount = amount * self.exchange_rates[from_curr][to_curr]

            # Displaying result
            self.output_label.setText(f"{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}")
        except ValueError:
            self.output_label.setText("Please enter a valid amount.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverter()
    window.show()
    sys.exit(app.exec_())
