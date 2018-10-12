attribute vec2 aVertexPosition;
uniform mat3 uProjectionMatId;
uniform mat3 uModelMat;
// vec3 pos = ...

void main() {

    //mat4 pro = mat4(uProjectionMatId);
    //mat4 model = mat4(uModelMat);

    mat3 move = uProjectionMatId * uModelMat;

    //gl_Position = vec4(aVertexPosition, 0, 1);

    gl_Position = mat4(move) * vec4(aVertexPosition.xy, 0, 1);

}