import React from "react";

import './App.css';
import TimeTable from "./TimeTable";

export default function App() {
  return (
    <div className="container">
      <div className="panel left">
        <TimeTable />
      </div>
      <div className="panel right">Right panel content goes here</div>
    </div>
  );
}