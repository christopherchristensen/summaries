/*
    Define a wire frame cube with methods for drawing it.

    * @param gl the webgl context
    * @param color the color of the cube
    * @returns object with draw method
    * @constructor
 */

function WireFrameCube(gl) {

    function defineVertices(gl) {
        var vertices = [

            // back
            -0.5,-0.5,-0.5, //v0
            -0.5,0.5,-0.5,  //v1
            -0.5,0.5,0.5,   //v2
            -0.5,-0.5,0.5,  //v3

            //left
            0.5,-0.5,-0.5,  //v4
            -0.5,-0.5,-0.5, //v0
            -0.5,-0.5,0.5,  //v3
            0.5,-0.5,0.5,   //v7

            //front
            0.5,-0.5,-0.5,  //v4
            0.5,0.5,-0.5,   //v5
            0.5,0.5,0.5,    //v6
            0.5,-0.5,0.5,   //v7

            //right
            0.5,0.5,-0.5,   //v5
            -0.5,0.5,-0.5,  //v1
            -0.5,0.5,0.5,   //v2
            0.5,0.5,0.5,    //v6

            //top
            0.5,-0.5,0.5,   //v7
            0.5,0.5,0.5,    //v6
            -0.5,0.5,0.5,   //v2
            -0.5,-0.5,0.5,  //v3

            //bottom
            0.5,-0.5,-0.5,  //v4
            0.5,0.5,-0.5,   //v5
            -0.5,0.5,-0.5,  //v1
            -0.5,-0.5,-0.5  //v0

        ];

        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);

        return buffer;
    }

    function defineNormal(gl) {
        var normalVertices = [
            // back
            -1,0,0,
            -1,0,0,
            -1,0,0,
            -1,0,0,

            // left
            0,-1,0,
            0,-1,0,
            0,-1,0,
            0,-1,0,

            // front
            1,0,0,
            1,0,0,
            1,0,0,
            1,0,0,

            // right
            0,1,0,
            0,1,0,
            0,1,0,
            0,1,0,

            // top
            0,0,1,
            0,0,1,
            0,0,1,
            0,0,1,

            // bottom
            0,0,-1,
            0,0,-1,
            0,0,-1,
            0,0,-1


        ];

        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(normalVertices), gl.STATIC_DRAW);

        return buffer;
    }

    function defineColor(gl) {

        var color = [

            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,

            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,

            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,

            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,

            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,

            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0,
            0.7, 0.5, 0.1, 1.0

        ];

        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(color), gl.STATIC_DRAW);

        return buffer;
    }

    function defineEdges(gl) {
        // Verbindung zwischen den Vertices
        var vertexIndices = [
            //back
            0,1,2,
            0,2,3,

            //left
            4,5,6,
            4,6,7,

            //front
            8,9,10,
            8,10,11,

            //right
            12,13,14,
            12,14,15,

            // top
            16,17,18,
            16,18,19,

            //bottom
            20,21,22,
            20,22,23
        ];

        var buffer = gl.createBuffer();
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(vertexIndices), gl.STATIC_DRAW);

        return buffer;
    }

    return {
        bufferVertices: defineVertices(gl),
        bufferNormalVertices: defineNormal(gl),
        bufferColor: defineColor(gl),
        bufferEdges: defineEdges(gl),
        draw: function(gl, aVertexPositionId, aColorPositionId, aNormalVertexId) {

            gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferVertices);
            gl.vertexAttribPointer(aVertexPositionId, 3, gl.FLOAT, false, 0, 0);
            gl.enableVertexAttribArray(aVertexPositionId);

            gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferNormalVertices);
            gl.vertexAttribPointer(aNormalVertexId,3, gl.FLOAT, false, 0, 0);
            gl.enableVertexAttribArray(aNormalVertexId);

            gl.bindBuffer(gl.ARRAY_BUFFER, this.bufferColor);
            gl.vertexAttribPointer(aColorPositionId, 4, gl.FLOAT, false, 0, 0);
            gl.enableVertexAttribArray(aColorPositionId);


            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.bufferEdges);
            gl.drawElements(gl.TRIANGLES, 36 ,gl.UNSIGNED_SHORT, 0);

        }
    }
}