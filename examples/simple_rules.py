"""
Example usage of simplified business rules
"""

from core.rules import RuleValidator, StateManager, ComputeEngine

# Example entity
order = {
    'status': 'draft',
    'items': [
        {'price': 10},
        {'price': 20}
    ]
}

# Basic validation
validator = RuleValidator()
rules = {
    'status': {'required': True},
    'items': {'min': 1}
}

is_valid = validator.validate_entity(order, rules)
print(f"Order valid: {is_valid}")

# Simple state transition
state_mgr = StateManager()
transitions = {
    'draft': ['submitted'],
    'submitted': ['approved', 'rejected']
}

can_submit = state_mgr.transition(order, 'submitted', transitions)
print(f"Order submitted: {can_submit}")

# Basic computation
compute = ComputeEngine()
total = compute.compute_sum(order['items'], 'price')
print(f"Order total: {total}")
