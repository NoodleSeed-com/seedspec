from dataclasses import dataclass
from typing import Optional, Dict, List, Union, Pattern
import re

@dataclass
class TypeConstraints:
    """Constraints for type validation"""
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    min_value: Optional[Union[int, float]] = None
    max_value: Optional[Union[int, float]] = None
    pattern: Optional[Pattern] = None
    
@dataclass
class Field:
    """Represents a field in a type definition"""
    name: str
    type: str  # 'str', 'num', 'bool', or custom type name
    constraints: Optional[TypeConstraints] = None
    format: Optional[str] = None  # '@email', '@url', etc
    is_integer: bool = False  # For num types
    is_array: bool = False
    item_type: Optional[str] = None  # For array types
    
@dataclass
class TypeDefinition:
    """Represents a complete type definition"""
    name: str
    fields: Dict[str, Field]
    
@dataclass
class ParseResult:
    """Result of parsing a Seed specification"""
    types: Dict[str, TypeDefinition]
    
class ValidationError(Exception):
    """Raised when type validation fails"""
    pass

class TypeSystem:
    """Core type system implementation"""
    VALID_FORMATS = {'email', 'url', 'uuid', 'date', 'time', 'phone'}
    
    @staticmethod
    def validate_field(field: Field, value: any) -> None:
        """Validate a value against field type and constraints"""
        if field.type == 'str':
            if not isinstance(value, str):
                raise ValidationError(f"Expected string for field {field.name}")
            
            if field.constraints:
                if (field.constraints.min_length is not None and 
                    len(value) < field.constraints.min_length):
                    raise ValidationError(
                        f"String too short for {field.name}: "
                        f"min length is {field.constraints.min_length}")
                
                if (field.constraints.max_length is not None and 
                    len(value) > field.constraints.max_length):
                    raise ValidationError(
                        f"String too long for {field.name}: "
                        f"max length is {field.constraints.max_length}")
                
                if field.constraints.pattern and not field.constraints.pattern.match(value):
                    raise ValidationError(
                        f"Invalid format for {field.name}: "
                        f"must match pattern {field.constraints.pattern.pattern}")
            
        elif field.type == 'num':
            try:
                num_value = int(value) if field.is_integer else float(value)
            except (ValueError, TypeError):
                raise ValidationError(
                    f"Expected {'integer' if field.is_integer else 'number'} "
                    f"for field {field.name}")
            
            if field.constraints:
                if (field.constraints.min_value is not None and 
                    num_value < field.constraints.min_value):
                    raise ValidationError(
                        f"Value too small for {field.name}: "
                        f"minimum is {field.constraints.min_value}")
                
                if (field.constraints.max_value is not None and 
                    num_value > field.constraints.max_value):
                    raise ValidationError(
                        f"Value too large for {field.name}: "
                        f"maximum is {field.constraints.max_value}")
                
        elif field.type == 'bool':
            if not isinstance(value, bool):
                raise ValidationError(f"Expected boolean for field {field.name}")
    
    @staticmethod
    def validate_format(format_name: str) -> None:
        """Validate a format specifier"""
        if not format_name.startswith('@'):
            raise ValidationError(f"Format must start with @: {format_name}")
        
        format_type = format_name[1:]
        if format_type not in TypeSystem.VALID_FORMATS:
            raise ValidationError(f"Unknown format type: {format_type}")
    
    @staticmethod
    def compile_pattern(pattern: str) -> Pattern:
        """Compile a regex pattern, raising ValidationError if invalid"""
        try:
            return re.compile(pattern)
        except re.error as e:
            raise ValidationError(f"Invalid regex pattern: {e}")
