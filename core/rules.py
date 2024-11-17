"""
Simplified business rules system for SeedML
"""

class RuleValidator:
    """Basic validation for simplified rules"""
    
    def validate_field(self, value, rules):
        """Validate a single field value"""
        if 'required' in rules and not value:
            return False
        if 'min' in rules and value < rules['min']:
            return False
        if 'max' in rules and value > rules['max']:
            return False
        return True

    def validate_entity(self, entity, rules):
        """Validate an entire entity"""
        for field, field_rules in rules.items():
            if not self.validate_field(entity.get(field), field_rules):
                return False
        return True

class StateManager:
    """Simple state transition management"""
    
    def can_transition(self, current_state, new_state, allowed_transitions):
        """Check if state transition is allowed"""
        return new_state in allowed_transitions.get(current_state, [])
    
    def transition(self, entity, new_state, allowed_transitions):
        """Attempt state transition"""
        if self.can_transition(entity['status'], new_state, allowed_transitions):
            entity['status'] = new_state
            return True
        return False

class ComputeEngine:
    """Basic computation engine"""
    
    def compute_sum(self, items, field):
        """Compute sum of a field across items"""
        return sum(item.get(field, 0) for item in items)
    
    def compute_count(self, items):
        """Count items"""
        return len(items)
