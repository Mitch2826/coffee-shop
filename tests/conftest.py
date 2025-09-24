import os
import sys
import pytest

# Ensure the project root (parent of tests/) is on sys.path for imports like `from order import Order`
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


@pytest.fixture(autouse=True)
def reset_order_state():
    # Import inside the fixture to avoid module-level import issues
    from order import Order
    Order.all_orders.clear()
    yield
    Order.all_orders.clear()
