# Types

Basic data types in SeedSpec with constraints.

```seed
types {
  text: {
    min: number
    max: number
    pattern?: regex
  }
  
  num: {
    min?: number
    max?: number
    integer?: boolean
  }

  bool: {}
}
```

Status: ✓ Available
