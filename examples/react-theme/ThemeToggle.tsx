import React from 'react';
import { useEffect } from 'react';

export function ThemeToggle() {
  const [isDark, setIsDark] = React.useState(() => 
    document.documentElement.classList.contains('dark')
  );
  
  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  }, [isDark]);
  
  return (
    <button
      onClick={() => setIsDark(!isDark)}
      className="
        bg-primary-500 dark:bg-primary-400
        text-white
        px-3 py-1 rounded-md text-sm
        transition-all hover:bg-primary-600 dark:hover:bg-primary-500
      "
    >
      {isDark ? '☀️ Light' : '🌙 Dark'}
    </button>
  );
}
