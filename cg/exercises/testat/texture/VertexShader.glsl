attribute vec3 aVertexPosition;
attribute vec4 aVertexColor;
varying vec4 vColor;
attribute vec2 aVertexTextureCoord;
varying vec2 vTextureCoord;

uniform mat4 modelMat;
uniform mat4 viewMat;
uniform mat4 projectionMat;

void main() {

    gl_Position   = projectionMat * viewMat * modelMat * vec4(aVertexPosition, 1);
    vColor        = aVertexColor;
    vTextureCoord = aVertexTextureCoord;

}
