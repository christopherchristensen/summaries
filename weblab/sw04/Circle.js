"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var Shape_1 = require("./Shape");
var Circle = /** @class */ (function (_super) {
    __extends(Circle, _super);
    function Circle(x, y, radius) {
        var _this = _super.call(this, x, y) || this;
        _this.radius = radius;
        return _this;
    }
    Circle.prototype.setRadius = function (radius) {
        this.radius = radius;
    };
    Circle.prototype.getRadius = function () {
        return this.radius;
    };
    Circle.prototype.draw = function () {
        return "Position(x:" + this.getX() + ", y:" + this.getY() + "), Radius: " + this.radius;
    };
    return Circle;
}(Shape_1.Shape));
exports.Circle = Circle;
//# sourceMappingURL=Circle.js.map