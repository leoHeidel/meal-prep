import React from "react";

function TimeTable() {
  const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

  return (
    <div>
      <h1>Time Table Content</h1>
      <div className="timetable-grid">
        {days.map((day) => (
          <div key={day} className="day">
            {day === "Monday" ? (
              <div className="widget">Recipe 1</div>
            ) : (
              <div className="day-widget">{day}</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default TimeTable;
