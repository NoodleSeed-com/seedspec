import React from 'react';

interface ButtonProps {
  variant?: 'primary' | 'secondary';
  children: React.ReactNode;
}

export function Button({ variant = 'primary', children }: ButtonProps) {
  const variantClasses = {
    primary: 'bg-primary-500 text-white hover:bg-primary-600',
    secondary: 'bg-secondary-500 text-white hover:bg-secondary-600'
  };
  
  return (
    <button 
      className={`
        ${variantClasses[variant]}
        text-base
        px-4 py-2 rounded-md
        transition-all duration-300
      `}
    >
      {children}
    </button>
  );
}
