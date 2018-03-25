import { Shape } from "./Shape";

class Circle extends Shape {
    private radius: number;
    constructor(x: number, y: number, radius: number) {
        super(x, y);
        this.radius = radius;
    }
    public setRadius(radius: number) {
        this.radius = radius;
    }
    public getRadius(): number {
        return this.radius;
    }
    public draw(): string {
        return "Position(x:" + this.getX() + ", y:" + this.getY() + "), Radius: " + this.radius;
    }
}

export { Circle };
