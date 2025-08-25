# ☕ Premium Coffee Machine

A modern, interactive coffee ordering system built with Python and Streamlit. This application simulates a real coffee machine where users can order different types of coffee, make payments using coins, and track resources.

![Coffee Machine Demo](https://img.shields.io/badge/Demo-Live-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

### ☕ Coffee Selection
- **Espresso**: Strong, concentrated coffee shot - $1.50
- **Latte**: Smooth coffee with steamed milk - $2.50  
- **Cappuccino**: Rich coffee with frothed milk - $3.00

### 💰 Payment System
- Accepts quarters ($0.25), dimes ($0.10), nickels ($0.05), and pennies ($0.01)
- Automatic change calculation
- Payment validation and error handling
- Money refund for insufficient payments

### 📊 Resource Management
- Real-time tracking of water, milk, and coffee supplies
- Color-coded resource status indicators
- Low resource warnings
- Admin controls for resource management

### 🎯 User Experience
- Intuitive web-based interface
- Responsive design for all devices
- Visual feedback and animations
- Clear error messages and status updates

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/coffee-machine.git
   cd coffee-machine
   ```

2. **Install required packages**
   ```bash
   pip install streamlit
   ```

3. **Run the application**
   ```bash
   streamlit run coffee_machine.py
   ```

4. **Open your browser**
   - The application will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL shown in your terminal

## 📱 How to Use

### For Customers:
1. **Select Your Drink**: Choose from Espresso, Latte, or Cappuccino
2. **Insert Coins**: Enter the number of quarters, dimes, nickels, and pennies
3. **Process Payment**: Click "Process Payment" to complete your order
4. **Enjoy**: Your coffee will be prepared and served!

### For Administrators:
- **Monitor Resources**: Check water, milk, and coffee levels in the sidebar
- **View Profits**: Track total earnings from all sales
- **Refill Resources**: Reset all resources to maximum capacity
- **Reset Profits**: Clear the profit counter

## 🏗️ Project Structure

```
coffee-machine/
│
├── coffee_machine.py          # Main Streamlit application
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
└── assets/                    # Images and other assets
    └── demo.gif              # Demo animation
```

## 🛠️ Technical Details

### Core Components

**Resource Management**
- Initial resources: 300L water, 200L milk, 100kg coffee
- Automatic resource deduction after each order
- Resource availability checking before order processing

**Payment Processing**
- Coin-based payment system with standard US denominations
- Precise decimal handling for accurate change calculation
- Transaction validation and error handling

**State Management**
- Streamlit session state for persistent data across interactions
- Real-time updates of resources and profits
- Form state management for payment processing

### Code Architecture

```python
# Key Functions
is_resource_available(ingredients)  # Check ingredient availability
process_payment(quarters, dimes, nickels, pennies)  # Calculate total payment
is_transaction_successful(money_received, drink_cost)  # Validate transaction
make_coffee(drink_name, ingredients)  # Process order and update resources
```

## 🎨 UI/UX Design

- **Modern Design**: Clean, coffee-themed interface with gradient backgrounds
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile devices  
- **Interactive Elements**: Hover effects, animations, and visual feedback
- **Accessibility**: Color-coded status indicators and clear typography
- **User-Friendly**: Intuitive navigation and clear call-to-action buttons



</div>
