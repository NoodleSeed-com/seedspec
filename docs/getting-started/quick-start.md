# Quick Start Guide

Get up and running with Seed Spec quickly.

## 1. Define Your App

Create a new file `app.seed`:

```javascript
// app.seed - Core app definition
app MyApp {
  // Define your core entities
  entity Product {
    name: string
    price: money
    stock: int
  }
  
  // Define your screens
  screen Products {
    list: [name, price, stock]
    actions: [create, edit, delete]
    filter: stock > 0
  }
  
  // Define component styles using Tailwind tokens
  theme {
    // Product list styles
    list {
      item: {
        bg: "white"
        border: "gray.200"
        hover: {
          bg: "gray.50"
        }
      }
      header: {
        bg: "gray.100"
        text: "gray.700"
        font: "semibold"
      }
    }

    // Action button styles
    button {
      primary: {
        bg: "blue.500"
        text: "white"
        hover: {
          bg: "blue.600"
        }
      }
      secondary: {
        bg: "gray.100"
        text: "gray.800"
        hover: {
          bg: "gray.200"
        }
      }
    }

    // Form input styles
    input {
      base: {
        bg: "white"
        border: "gray.300"
        text: "gray.900"
        focus: {
          border: "blue.500"
          ring: "blue.500"
        }
      }
    }
  }
}
```

## 2. Run the Generator

```bash
seed generate app.seed
```

This will:
- Generate a full-stack application
- Compile theme tokens to Tailwind classes
- Set up database and API endpoints
- Create React components with theme integration

## 3. Start the App

```bash
seed start
```

Your app is now running at http://localhost:3000 with:
- Styled components using your theme
- Dark mode support out of the box
- Responsive design
- Form validation
- API integration

## Next Steps

1. Add more entities and screens
2. Define business rules
3. Customize component themes
4. Add integrations

See the [Full Guide](first-app.md) for a more detailed walkthrough.
