"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Shape = /** @class */ (function () {
    function Shape(x, y) {
        this.x = x;
        this.y = y;
    }
    Shape.prototype.setX = function (x) {
        this.x = x;
    };
    Shape.prototype.setY = function (y) {
        this.y = y;
    };
    Shape.prototype.getX = function () {
        return this.x;
    };
    Shape.prototype.getY = function () {
        return this.y;
    };
    return Shape;
}());
exports.Shape = Shape;
//# sourceMappingURL=Shape.js.map