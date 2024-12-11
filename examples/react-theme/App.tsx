import { ThemeProvider } from "./ThemeContext";
import { useTheme } from "./ThemeContext";
import "./theme.css";

function DemoCard({ title, children }: { title: string; children: React.ReactNode }) {
  const theme = useTheme();
  return (
    <div style={{
      backgroundColor: theme.colors.surface,
      padding: theme.spacing.lg,
      borderRadius: theme.borders.radius.lg,
      boxShadow: theme.shadows.md,
      marginBottom: theme.spacing.md
    }}>
      <h2 style={{
        color: theme.colors.text,
        fontSize: theme.typography.fontSize.xl,
        fontWeight: theme.typography.fontWeight.bold,
        marginBottom: theme.spacing.md
      }}>{title}</h2>
      {children}
    </div>
  );
}

function Button({ children, primary = false }: { children: React.ReactNode; primary?: boolean }) {
  const theme = useTheme();
  return (
    <button style={{
      backgroundColor: primary ? theme.colors.primary : theme.colors.surface,
      color: primary ? "#fff" : theme.colors.text,
      padding: `${theme.spacing.sm} ${theme.spacing.md}`,
      borderRadius: theme.borders.radius.md,
      border: primary ? "none" : `${theme.borders.width.thin} solid ${theme.colors.border}`,
      fontSize: theme.typography.fontSize.base,
      fontWeight: theme.typography.fontWeight.medium,
      cursor: "pointer",
      marginRight: theme.spacing.sm
    }}>
      {children}
    </button>
  );
}

function App() {
  const theme = useTheme();
  
  return (
    <div style={{
      backgroundColor: theme.colors.background,
      minHeight: "100vh",
      padding: theme.spacing.xl,
      fontFamily: theme.typography.fontFamily.base
    }}>
      <h1 style={{
        color: theme.colors.text,
        fontSize: theme.typography.fontSize.xl,
        marginBottom: theme.spacing.xl
      }}>Theme Demo</h1>

      <DemoCard title="Buttons">
        <Button primary>Primary Button</Button>
        <Button>Secondary Button</Button>
      </DemoCard>

      <DemoCard title="Typography">
        <div style={{ color: theme.colors.text }}>
          <p style={{ fontSize: theme.typography.fontSize.base, marginBottom: theme.spacing.sm }}>
            Base text size with normal weight
          </p>
          <p style={{ 
            fontSize: theme.typography.fontSize.lg,
            fontWeight: theme.typography.fontWeight.medium,
            marginBottom: theme.spacing.sm
          }}>
            Larger text with medium weight
          </p>
          <p style={{ 
            fontSize: theme.typography.fontSize.sm,
            color: theme.colors.textLight
          }}>
            Smaller text in lighter color
          </p>
        </div>
      </DemoCard>

      <DemoCard title="Colors">
        <div style={{ display: "flex", gap: theme.spacing.md, flexWrap: "wrap" }}>
          {Object.entries(theme.colors).map(([name, color]) => (
            <div key={name} style={{
              padding: theme.spacing.sm,
              backgroundColor: color,
              border: `${theme.borders.width.thin} solid ${theme.colors.border}`,
              borderRadius: theme.borders.radius.sm,
              width: "100px",
              textAlign: "center",
              color: name === "background" || name === "surface" ? theme.colors.text : "#fff"
            }}>
              {name}
            </div>
          ))}
        </div>
      </DemoCard>
    </div>
  );
}

export default function ThemedApp() {
  return (
    <ThemeProvider>
      <App />
    </ThemeProvider>
  );
}
