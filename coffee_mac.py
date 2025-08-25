import streamlit as st
import time

# Initialize session state
if 'resources' not in st.session_state:
    st.session_state.resources = {
        "Water": 300000,
        "Milk": 200000,
        "coffee": 100000,
    }

if 'profit' not in st.session_state:
    st.session_state.profit = 0

if 'order_status' not in st.session_state:
    st.session_state.order_status = ""

if 'show_payment' not in st.session_state:
    st.session_state.show_payment = False

if 'selected_drink' not in st.session_state:
    st.session_state.selected_drink = None

# Menu configuration
MENU = {
    "Espresso": {
        "Ingredients": {
            "Water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
        "emoji": "☕",
        "description": "A strong, concentrated coffee shot"
    },
    "Latte": {
        "Ingredients": {
            "Water": 200,
            "Milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
        "emoji": "🥛",
        "description": "Smooth coffee with steamed milk"
    },
    "Cappuccino": {
        "Ingredients": {
            "Water": 250,
            "Milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
        "emoji": "☕",
        "description": "Rich coffee with frothed milk"
    },
}

def is_resource_available(ingredients):
    """Returns True if the ingredients are available"""
    for item in ingredients:
        if ingredients[item] > st.session_state.resources[item]:
            return False, f"Sorry, we don't have enough {item.lower()}"
    return True, "Resources available"

def process_payment(quarters, dimes, nickels, pennies):
    """Returns the total amount of coins"""
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the transaction was successful"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        st.session_state.profit += drink_cost
        return True, change
    else:
        return False, 0

def make_coffee(drink_name, ingredients):
    """Makes coffee by updating resources"""
    for item in ingredients:
        st.session_state.resources[item] -= ingredients[item]
    return f"Here is your {drink_name} {MENU[drink_name]['emoji']}! Enjoy!"

# Streamlit UI
st.set_page_config(
    page_title="☕ Coffee Machine",
    page_icon="☕",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #8B4513, #D2B48C);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .drink-card {
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: #f9f9f9;
        transition: all 0.3s ease;
    }
    
    .drink-card:hover {
        border-color: #8B4513;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .resource-low {
        color: #ff4444;
        font-weight: bold;
    }
    
    .resource-ok {
        color: #44ff44;
        font-weight: bold;
    }
    
    .profit-display {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>☕ Premium Coffee Machine ☕</h1>
    <p>Welcome to your favorite coffee destination!</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for machine status and admin
with st.sidebar:
    st.header("🔧 Machine Status")
    
    # Resources display
    st.subheader("📊 Resources")
    for resource, amount in st.session_state.resources.items():
        unit = "ml" if resource != "coffee" else "g"
        color_class = "resource-low" if amount < 1000 else "resource-ok"
        st.markdown(f"**{resource}**: <span class='{color_class}'>{amount:,} {unit}</span>", 
                   unsafe_allow_html=True)
    
    st.divider()
    
    # Profit display
    st.markdown(f"""
    <div class="profit-display">
        <h3>💰 Total Profit</h3>
        <h2>${st.session_state.profit:.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Admin controls
    st.subheader("🔑 Admin Controls")
    if st.button("🔄 Refill Resources"):
        st.session_state.resources = {
            "Water": 300000,
            "Milk": 200000,
            "coffee": 100000,
        }
        st.success("Resources refilled!")
        st.rerun()
    
    if st.button("💸 Reset Profit"):
        st.session_state.profit = 0
        st.success("Profit reset!")
        st.rerun()

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("☕ Select Your Drink")
    
    # Display drinks in a grid
    for drink_name, drink_info in MENU.items():
        with st.container():
            st.markdown(f'<div class="drink-card">', unsafe_allow_html=True)
            
            drink_col1, drink_col2, drink_col3 = st.columns([1, 2, 1])
            
            with drink_col1:
                st.markdown(f"<h2 style='text-align: center;'>{drink_info['emoji']}</h2>", 
                           unsafe_allow_html=True)
            
            with drink_col2:
                st.subheader(drink_name)
                st.write(drink_info['description'])
                
                # Show ingredients
                ingredients_text = ", ".join([f"{amount}{('ml' if ingredient != 'coffee' else 'g')} {ingredient.lower()}" 
                                            for ingredient, amount in drink_info['Ingredients'].items()])
                st.caption(f"Ingredients: {ingredients_text}")
                
                st.markdown(f"**Price: ${drink_info['cost']:.2f}**")
            
            with drink_col3:
                if st.button(f"Order {drink_name}", key=f"order_{drink_name}"):
                    # Check if resources are available
                    available, message = is_resource_available(drink_info['Ingredients'])
                    if available:
                        st.session_state.selected_drink = drink_name
                        st.session_state.show_payment = True
                    else:
                        st.error(message)
                        st.session_state.order_status = message
            
            st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.session_state.show_payment and st.session_state.selected_drink:
        st.header("💰 Payment")
        drink = MENU[st.session_state.selected_drink]
        
        st.info(f"Selected: {st.session_state.selected_drink} - ${drink['cost']:.2f}")
        
        with st.form("payment_form"):
            st.subheader("Insert Coins")
            
            col_q, col_d = st.columns(2)
            with col_q:
                quarters = st.number_input("Quarters ($0.25)", min_value=0, value=0, step=1)
            with col_d:
                dimes = st.number_input("Dimes ($0.10)", min_value=0, value=0, step=1)
            
            col_n, col_p = st.columns(2)
            with col_n:
                nickels = st.number_input("Nickels ($0.05)", min_value=0, value=0, step=1)
            with col_p:
                pennies = st.number_input("Pennies ($0.01)", min_value=0, value=0, step=1)
            
            total_inserted = process_payment(quarters, dimes, nickels, pennies)
            st.write(f"**Total inserted: ${total_inserted:.2f}**")
            st.write(f"**Amount needed: ${drink['cost']:.2f}**")
            
            submitted = st.form_submit_button("💳 Process Payment", type="primary")
            cancel = st.form_submit_button("❌ Cancel Order")
            
            if cancel:
                st.session_state.show_payment = False
                st.session_state.selected_drink = None
                st.rerun()
            
            if submitted:
                success, change = is_transaction_successful(total_inserted, drink['cost'])
                if success:
                    coffee_message = make_coffee(st.session_state.selected_drink, drink['Ingredients'])
                    st.success(coffee_message)
                    if change > 0:
                        st.info(f"Your change: ${change:.2f}")
                    
                    # Reset payment form
                    st.session_state.show_payment = False
                    st.session_state.selected_drink = None
                    
                    # Show success animation
                    with st.empty():
                        for i in range(3):
                            st.write("☕" * (i + 1) + " Preparing your coffee... " + "☕" * (i + 1))
                            time.sleep(0.5)
                    
                    st.rerun()
                else:
                    st.error("Insufficient payment! Money refunded.")
    
    elif not st.session_state.show_payment:
        st.header("ℹ️ How to Order")
        st.info("""
        1. 🎯 Select your favorite drink
        2. 💰 Insert coins for payment
        3. ☕ Enjoy your freshly brewed coffee!
        
        **Accepted Coins:**
        - Quarters ($0.25)
        - Dimes ($0.10) 
        - Nickels ($0.05)
        - Pennies ($0.01)
        """)

# Status messages
if st.session_state.order_status:
    st.warning(st.session_state.order_status)
    if st.button("Clear Message"):
        st.session_state.order_status = ""
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>☕ Premium Coffee Machine | Serving quality coffee since 2024 ☕</p>
</div>
""", unsafe_allow_html=True)