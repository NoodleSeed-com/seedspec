import { useState, useCallback } from 'react';




export function useTask() {
  
  
  
  const [items, setItems] = useState(() => {
    const saved = localStorage.getItem('tasks');
    return saved ? JSON.parse(saved) : [];
  });

  // Persist to localStorage whenever items change
  const persistItems = useCallback((newItems) => {
    localStorage.setItem('tasks', JSON.stringify(newItems));
    setItems(newItems);
  }, []);

  const create = useCallback((data) => {
    const defaults = {
      
      title: null,
      
    };
    const newItems = [...items, { ...defaults, ...data, id: Date.now().toString() }];
    persistItems(newItems);
  }, [items, persistItems]);

  const update = useCallback((id, data) => {
    const newItems = items.map(item => 
      item.id === id ? { ...item, ...data } : item
    );
    persistItems(newItems);
  }, [items, persistItems]);

  const remove = useCallback((id) => {
    const newItems = items.filter(item => item.id !== id);
    persistItems(newItems);
  }, [items, persistItems]);

  return { items, create, update, remove };
}