import { Circle } from "./Circle";
import { Rectangle } from "./Rectangle";

const circle = new Circle(1, 2, 5);
const rectangle = new Rectangle(1, 2, 4, 5);

circle.setRadius(6);
rectangle.setWidth(2);
rectangle.setHeight(4);

document.body.innerHTML = circle.draw() + "<br>" + rectangle.draw();
