/**
 * Created by toko on 13.05.17.
 */

/**
 *
 * Define a wire frame cube with methods for drawing it.
 *
 * @param gl
 * @param color the color of the cube
 * @returns object with draw method
 * @constructor
 */
function WireFrameCube(gl, color) {
    function defineVertices(gl) {
        // define the vertices of the cube
        var vertices = [
            -0.5,-0.5,-0.5,      // v0
             0.5,-0.5,-0.5,      // v1
             0.5, 0.5,-0.5,      // v2
            -0.5, 0.5,-0.5,      // v3
            -0.5,-0.5, 0.5,      // v4
             0.5,-0.5, 0.5,      // v5
             0.5, 0.5, 0.5,      // v6
            -0.5, 0.5, 0.5       // v7
        ];
        var buffer  = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
        return buffer;
    }


    function defineEdges(gl) {
        // define the edges for the cube, there are 12 edges in a cube
        var vertexIndices = [
            0,1, // face on z = 0
            1,2,
            2,3,
            3,0,
            4,5, // face on z = 1
            5,6,
            6,7,
            7,4,
            0,4, // edges between
            1,5,
            2,6,
            3,7
        ];
        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(vertexIndices), gl.STATIC_DRAW);

        return buffer;
    }

    return {
        bufferVertices: defineVertices(gl),
        bufferEdges: defineEdges(gl),
        color: color,

        draw: function(gl, aVertexPositionId, aVertexColorId) {
            // bind the buffer, so that the cube vertices are used
            gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferVertices);
            gl.vertexAttribPointer(aVertexPositionId, 3, gl.FLOAT, false, 0, 0);
            gl.enableVertexAttribArray(aVertexPositionId);

            // set a constant color for all vertices
            gl.disableVertexAttribArray(aVertexColorId);
            gl.vertexAttrib3fv(aVertexColorId, this.color);

            // bind the element array
            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.bufferEdges);
            gl.drawElements(gl.LINES, 24 ,gl.UNSIGNED_SHORT, 0);

        }
    }
}



