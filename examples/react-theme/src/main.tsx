import React from 'react'
import ReactDOM from 'react-dom/client'
import { ThemeProvider } from '../ThemeContext'
import { Button } from '../ExampleButton'
import { ThemeToggle } from '../ThemeToggle'
import { useTailwindColor } from '../ThemeContext'
import './index.css'

function App() {
  const colors = useTailwindColor('background');
  const textColors = useTailwindColor('text');
  
  return (
    <div className={`min-h-screen ${colors.bg} ${textColors.text} transition-colors`}>
      <div className="container mx-auto p-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-2xl font-bold">Theme Example</h1>
          <ThemeToggle />
        </div>
        <div className="space-x-4">
          <Button variant="primary">Primary Button</Button>
          <Button variant="secondary">Secondary Button</Button>
        </div>
      </div>
    </div>
  )
}

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ThemeProvider>
      <App />
    </ThemeProvider>
  </React.StrictMode>
)
