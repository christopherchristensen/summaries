import { Shape } from "./Shape";

class Rectangle extends Shape {
    private width: number;
    private height: number;
    constructor(x: number, y: number, width: number, height: number) {
        super(x, y);
        this.width = width;
        this.height = height;
    }
    public setWidth(width: number) {
        this.width = width;
    }
    public setHeight(height: number) {
        this.height = height;
    }
    public getWidth(): number {
        return this.width;
    }
    public getHeight(): number {
        return this.height;
    }
    public draw(): string {
        return "Position(x:" + this.getX() + ", y:" + this.getY() + "), Measurements(width: "
            + this.width + ", height: " + this.height + ")";
    }
}

export { Rectangle };
