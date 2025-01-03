import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';

import { Tasks } from './screens/Tasks';


export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow-lg">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="flex-shrink-0 flex items-center">
                  <span className="text-xl font-bold text-gray-800">SeedSpec App</span>
                </div>
                <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                  
                  <Link 
                    to="/tasks"
                    className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
                  >
                    Tasks
                  </Link>
                  
                </div>
              </div>
            </div>
          </div>
        </nav>

        <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          <Switch>
            
            <Route path="/tasks" component={ Tasks } />
            
          </Switch>
        </main>
      </div>
    </Router>
  );
}