import React from "react";

import './TimeTable.css';


function TimeTable() {
    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

    return (
      <div>
        <h1>Time Table Content</h1>
        <div className="timetable-grid">
          {days.map((day) => (
            <div key={day} className="day">
              <div className="widgets">
                <div className="day-widget">{day}</div>
                {day === "Monday" ? (
                  <div className="recipe-widget">Recipe 1</div>
                ) : null}
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }


export default TimeTable;
