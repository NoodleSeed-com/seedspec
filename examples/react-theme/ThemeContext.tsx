import { createContext, useContext, ReactNode, useState, useEffect } from 'react';

// Original theme specification
export const theme = {} as const;

// Tailwind class mapping
export const tailwindMapping = {} as const;

export type Theme = typeof theme;
export type TailwindMapping = typeof tailwindMapping;

interface ThemeContextValue {
  theme: Theme;
  tailwind: TailwindMapping;
  currentMode?: string;
  setMode: (mode: string) => void;
}

const ThemeContext = createContext<ThemeContextValue>({
  theme,
  tailwind: tailwindMapping,
  setMode: () => {}
});

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [currentMode, setCurrentMode] = useState<string | undefined>(
    typeof window !== 'undefined' 
      ? localStorage.getItem('theme-mode') ?? undefined
      : undefined
  );

  useEffect(() => {
    if (currentMode) {
      document.documentElement.setAttribute('data-theme', currentMode);
      localStorage.setItem('theme-mode', currentMode);
    }
  }, [currentMode]);

  return (
    <ThemeContext.Provider 
      value={{
        theme,
        tailwind: tailwindMapping,
        currentMode,
        setMode: setCurrentMode
      }}
    >
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}

// Utility hooks for Tailwind classes
export function useTailwindColor(colorKey: string) {
  const { tailwind } = useTheme();
  return tailwind[`colors.${colorKey}`] ?? {};
}

export function useTailwindTypography(key: string) {
  const { tailwind } = useTheme();
  return tailwind[`typography.${key}`] ?? '';
}

export function useTailwindAnimation(key: string) {
  const { tailwind } = useTheme();
  return tailwind[`animation.${key}`] ?? '';
}
