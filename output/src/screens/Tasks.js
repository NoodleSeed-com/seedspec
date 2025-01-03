import React, { useState } from 'react';
import { useTask } from '../models/Task';

export function Tasks() {
  const { items, create, update, remove } = useTask();
  const [editingId, setEditingId] = useState(null);

  return (
    <div className="bg-white shadow rounded-lg">
      <div className="px-4 py-5 sm:p-6">
        <h1 className="text-2xl font-bold text-gray-900 mb-8">Tasks</h1>
        
        {/* Create Form */}
        <div className="bg-gray-50 rounded-lg p-6 mb-8">
          <h2 className="text-lg font-medium text-gray-900 mb-4">Create New Task</h2>
          <form 
            className="space-y-6"
            onSubmit={e => {
              e.preventDefault();
              const formData = new FormData(e.target);
              const data = Object.fromEntries(formData);
              create(data);
              e.target.reset();
            }}
          >
            
            <div>
              <label className="block text-sm font-medium text-gray-700">
                Title
              </label>
              <input 
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                name="title"
                type="text"
                
                required
                
                
              />
            </div>
            
            <button 
              type="submit"
              className="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
            >
              Create
            </button>
          </form>
        </div>

        {/* List */}
        <div className="space-y-4">
          {items.map(item => (
            <div 
              key={item.id}
              className="bg-white shadow rounded-lg overflow-hidden border border-gray-200"
            >
              {editingId === item.id ? (
                <form 
                  className="p-4"
                  onSubmit={e => {
                    e.preventDefault();
                    const formData = new FormData(e.target);
                    const data = Object.fromEntries(formData);
                    update(item.id, data);
                    setEditingId(null);
                  }}
                >
                  
                  <div className="mb-4">
                    <label className="block text-sm font-medium text-gray-700">
                      Title
                    </label>
                    <input
                      className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                      name="title"
                      type="text"
                      defaultValue={item.title !== undefined ? item.title : null}
                      required
                      
                      
                    />
                  </div>
                  
                  <div className="flex gap-2">
                    <button 
                      type="submit"
                      className="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                    >
                      Save
                    </button>
                    <button
                      type="button"
                      onClick={() => setEditingId(null)}
                      className="inline-flex justify-center rounded-md border border-gray-300 bg-white py-2 px-4 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                    >
                      Cancel
                    </button>
                  </div>
                </form>
              ) : (
                <div className="p-4">
                  <div className="flex items-center justify-between">
                    <div className="space-y-1">
                      
                      <div>
                        <span className="text-sm font-medium text-gray-500">Title:</span>
                        <span className="ml-2 text-sm text-gray-900">
                          {item.title !== undefined ? item.title.toString() : ''}
                        </span>
                      </div>
                      
                    </div>
                    <div className="flex gap-2">
                      <button
                        onClick={() => setEditingId(item.id)}
                        className="inline-flex items-center rounded-md border border-gray-300 bg-white px-3 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                      >
                        Edit
                      </button>
                      <button 
                        onClick={() => remove(item.id)}
                        className="inline-flex items-center rounded-md border border-transparent bg-red-600 px-3 py-2 text-sm font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}