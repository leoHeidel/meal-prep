import React, { useRef } from "react";
import { useDrag, useDrop } from "react-dnd";
import { ItemTypes } from "./ItemTypes";

const style = {
  border: "1px dashed gray",
  padding: "0.5rem 1rem",
  marginLeft: ".5rem",
  backgroundColor: "white",
  cursor: "move",
};


export const Recipe = ({ id, day, text, index, moveRecipe }) => {
  const ref = useRef(null);
  const [{ handlerId }, drop] = useDrop({
    accept: ItemTypes.RECIPE,
    collect(monitor) {
      return {
        handlerId: monitor.getHandlerId(),
      };
    },
    hover(item, monitor) {
      if (!ref.current) {
        return;
      }
      const dragIndex = item.index;
      const hoverIndex = index;
      const dragDay = item.day;
      const hoverDay = day;
      // Don't replace items with themselves
      if (dragIndex === hoverIndex && dragDay === hoverDay) {
        return;
      }

      moveRecipe(dragIndex, hoverIndex, hoverDay);
      item.index = hoverIndex;
    },
  });

  const [{ isDragging }, drag] = useDrag({
    type: ItemTypes.RECIPE,
    item: () => {
      return { id, day, index };
    },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
  });

  const opacity = isDragging ? 0 : 1;
  drag(drop(ref));
  return (
    <div ref={ref} style={{ ...style, opacity }} data-handler-id={handlerId}>
      {text}
    </div>
  );
};

// export const Day = (day)
