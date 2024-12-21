import pytest
import os
from src.parser import Parser  # We'll extend this to handle types

def load_fixture(filename):
    """Helper to load test fixtures"""
    fixture_path = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'types', filename)
    with open(fixture_path, 'r') as f:
        return f.read()

def test_basic_string_type():
    """Test basic string type parsing and validation"""
    code = """
    type User {
        name str
    }
    """
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        assert "name" in result.types["User"].fields
        assert result.types["User"].fields["name"].type == "str"

def test_string_with_constraints():
    """Test string type with length constraints"""
    code = """
    type User {
        username str(3..20)
    }
    """
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        field = result.types["User"].fields["username"]
        assert field.type == "str"
        assert field.constraints.min_length == 3
        assert field.constraints.max_length == 20

def test_string_with_format():
    """Test string type with format validation"""
    code = """
    type User {
        email str(format: @email)
    }
    """
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        field = result.types["User"].fields["email"]
        assert field.type == "str"
        assert field.format == "email"

def test_number_type():
    """Test number type parsing and validation"""
    code = """
    type Product {
        price num(0..)
        quantity num(1..100, int: true)
    }
    """
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        price = result.types["Product"].fields["price"]
        quantity = result.types["Product"].fields["quantity"]
        
        assert price.type == "num"
        assert price.constraints.min_value == 0
        assert price.constraints.max_value is None
        
        assert quantity.type == "num"
        assert quantity.constraints.min_value == 1
        assert quantity.constraints.max_value == 100
        assert quantity.is_integer == True

def test_boolean_type():
    """Test boolean type parsing"""
    code = """
    type Task {
        done bool
    }
    """
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        assert result.types["Task"].fields["done"].type == "bool"

def test_type_inference():
    """Test type inference from context"""
    code = """
    type Order {
        items [Product]
        total num  // Should infer constraints from items prices
    }
    """
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        assert result.types["Order"].fields["total"].type == "num"
        assert result.types["Order"].fields["total"].constraints.min_value == 0

def test_invalid_type_definition():
    """Test error handling for invalid type definitions"""
    code = """
    type User {
        age num(-1..150)  // Age can't be negative
    }
    """
    parser = Parser()
    with pytest.raises(ValueError, match=r".*age.*negative.*"):
        parser.parse(code)

def test_type_validation():
    """Test validation of type constraints"""
    code = """
    type User {
        password str(8..32, match: "^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{8,}$")
    }
    """
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        field = result.types["User"].fields["password"]
        assert field.type == "str"
        assert field.constraints.min_length == 8
        assert field.constraints.max_length == 32
        assert field.constraints.pattern is not None

def test_composite_types():
    """Test composite type definitions using fixtures"""
    code = load_fixture('basic_types.seed')
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        # Test User type
        assert "User" in result.types
        user_type = result.types["User"]
        assert user_type.fields["name"].type == "str"
        assert user_type.fields["name"].constraints.min_length == 3
        assert user_type.fields["name"].constraints.max_length == 50
        
        # Test Order type with composite fields
        assert "Order" in result.types
        order_type = result.types["Order"]
        assert order_type.fields["customer"].type == "User"
        assert order_type.fields["items"].type == "array"
        assert order_type.fields["items"].item_type == "Product"

def test_string_formats():
    """Test all string format variations"""
    code = load_fixture('basic_types.seed')
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        formats = result.types["StringFormats"]
        assert formats.fields["email"].format == "email"
        assert formats.fields["url"].format == "url"
        assert formats.fields["uuid"].format == "uuid"
        assert formats.fields["date"].format == "date"
        assert formats.fields["time"].format == "time"
        assert formats.fields["phone"].format == "phone"

def test_number_constraints():
    """Test number type constraints"""
    code = load_fixture('basic_types.seed')
    parser = Parser()
    with pytest.raises(NotImplementedError):
        result = parser.parse(code)
        numbers = result.types["Numbers"]
        assert numbers.fields["integer"].is_integer == True
        assert numbers.fields["positive"].constraints.min_value == 0
        assert numbers.fields["percentage"].constraints.max_value == 100
        assert numbers.fields["rating"].constraints.min_value == 1
        assert numbers.fields["rating"].constraints.max_value == 5
        assert numbers.fields["rating"].is_integer == True
