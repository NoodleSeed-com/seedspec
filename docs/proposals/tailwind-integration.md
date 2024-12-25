# Candidate Proposal: Tailwind CSS Integration for Seed

## Overview

This document proposes a method for integrating Tailwind CSS utility classes into the Seed language, allowing developers to leverage Tailwind's styling system within Seed applications.

## Motivation

Tailwind CSS has gained significant popularity due to its utility-first approach, which enables rapid UI development and promotes consistency. Integrating Tailwind with Seed would provide the following benefits:

-   **Faster Development:**  Developers can quickly style components using Tailwind's extensive utility classes.
-   **Consistency:**  Tailwind's predefined design system ensures a consistent look and feel across Seed applications.
-   **Customization:**  Tailwind's configuration options allow for easy customization of the design system.
-   **Reduced Boilerplate:**  Using utility classes reduces the need to write custom CSS, leading to smaller and more maintainable codebases.

## Proposed Solution

The proposed solution introduces a special `tailwind` block within Seed components and applications, allowing developers to specify Tailwind classes for styling.

### Syntax

```seed
// Define a component with Tailwind styles
component Button {
  tailwind {
    base: "px-4 py-2 rounded-md font-semibold" // Default Tailwind classes
    variants: {
      primary: {
        base: "bg-blue-500 text-white",
        hover: "bg-blue-600",
        focus: "ring-2 ring-blue-500 ring-offset-2"
      },
      secondary: {
        base: "bg-gray-100 text-gray-800",
        hover: "bg-gray-200",
        focus: "ring-2 ring-gray-500 ring-offset-2"
      }
    },
    sizes: {
      small: "px-2 py-1 text-sm",
      medium: "px-4 py-2",
      large: "px-6 py-3 text-lg"
    }
  }
}

// Define an application with global Tailwind overrides
app TailwindApp {
  tailwind {
    base: "font-sans text-gray-900" // Applies to the whole app
    components: {
      Button: { // Override Button defaults
        base: "px-5 py-3 rounded-lg font-bold"
      }
    }
  }

  // Screen-level overrides
  screen MyScreen {
    tailwind {
      components: {
        Button: {
          variants: {
            primary: {
              base: "bg-green-500 text-white"
            }
          }
        }
      }
    }

    // Use components with Tailwind styles
    Button {
      variant: "primary"
      size: "large"
    }
  }
}
```

### Implementation Details

1. **Parsing:**  The Seed compiler would need to be extended to parse the  `tailwind`  block and extract the Tailwind classes.
2. **Class Mapping:**  A mapping mechanism would be required to associate Tailwind classes with their corresponding CSS properties. This could be achieved by:
    
    -   Using a predefined mapping table.
    
    -   Integrating with Tailwind's configuration file (tailwind.config.js) to dynamically generate the mapping.
    
3. **Style Generation:**  During the compilation process to React components (or other target platforms), the compiler would generate the appropriate CSS styles based on the Tailwind classes and the mapping mechanism. This could involve:
    
    -   Generating inline styles.
    
    -   Creating CSS modules with the generated styles.
    
    -   Utilizing a CSS-in-JS library that supports Tailwind.
    
4. **Default Styles:**  Seed could provide a set of default Tailwind styles for common components, which could be overridden at the application or screen level.
5. **Overrides:**  The  `tailwind`  block would support overrides at different levels (application, screen, component), allowing for granular control over styling.

### Example

See the `examples/tailwind-candidate.seed` file for a complete example demonstrating the proposed syntax and usage.

## Open Questions

1. **Performance:**  How would the use of Tailwind classes impact the performance of Seed applications, especially in terms of bundle size and rendering speed?
2. **Integration with Existing CSS:**  How would the Tailwind integration interact with existing CSS styles defined in Seed applications?
3. **Tooling:**  What kind of tooling support would be needed to provide a good developer experience (e.g., autocompletion, linting)?

## Conclusion

This proposal outlines a candidate approach for integrating Tailwind CSS into Seed. It aims to provide a flexible and efficient way to style Seed applications while leveraging the benefits of Tailwind's utility-first system. Further discussion and experimentation are needed to refine the proposal and address the open questions.
