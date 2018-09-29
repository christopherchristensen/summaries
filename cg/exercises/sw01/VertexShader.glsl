// Schritt 1: Spezifikation des entsprechenden Attributes im Vertex Shader Program (aVertexPosition)
attribute vec2 aVertexPosition;


void main () {

    gl_Position = vec4 (aVertexPosition, 0, 1);

}