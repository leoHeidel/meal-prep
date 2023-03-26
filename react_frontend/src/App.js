// App.js
import React from 'react';
import './App.css';
import TimeTable from './TimeTable';
import Mealdetail from './Mealdetail';
import '@fortawesome/fontawesome-free/css/all.css';

export default function App() {
  return (
    <div className="container">
      <div className="panel left">
        <TimeTable />
      </div>
      <div className="panel right">
        <Mealdetail /> {/* Include the Mealdetail component */}
      </div>
    </div>
  );
}
