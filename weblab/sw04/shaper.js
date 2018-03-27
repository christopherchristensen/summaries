"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Circle_1 = require("./Circle");
var Rectangle_1 = require("./Rectangle");
var circle = new Circle_1.Circle(1, 2, 5);
var rectangle = new Rectangle_1.Rectangle(1, 2, 4, 5);
circle.setRadius(6);
rectangle.setWidth(2);
rectangle.setHeight(4);
document.body.innerHTML = circle.draw() + "<br>" + rectangle.draw();
//# sourceMappingURL=shaper.js.map