
/*
Rotate Matrix 1.7
Given an image represented by an N x N Matrix, where each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degress in place





Solution: Perform a swap on each layer. Start with the outer most layer and work
inwards. The number of "layers" is N / 2

e.g. a 4 x 4 layer has 2 layers

Do the following
tmp = top[i]
top[i] = left[i]
bottom[i] = right[i]
right[i] = tmp
*/

/*
Solution: Perform a swap on each layer of the matrix starting form the outermost
layer and working your way in

Within each layer, then do a cell by cell swap

(bottom)left -> top
bottom(right) -> bottom(left)
right(top) -> right(bottom)
top(left) -> (top)right

For each layer find an offset of how much you should be moving it. The offset
allows to you to understand which one you need i.e. end - offset if offset is
0 then you can swap with the edges of the graph i.e. 2 - 0
*/

function rotateMatrix_(matrix) {
  let n = matrix.length;
  // rotate for each layer
  for (layer = 0; layer < n / 2; layer++) {
    let start = layer;
    let end = n - 1 - layer;
     for (let j = start; j < end; j++) {
       let offset = j - start;
       let top = matrix[start][j];

       // left -> top
       matrix[start][j] = matrix[end - offset][start];

       // bottom -> left
       matrix[end - offset][j] = matrix[last][last - offset];

       // right -> bottom
       matrix[end][end - offset] = matrix[j][end]

       // top
       matrix[j][last] = top;
     }
  }
}







var rotateMatrixAlt = function(matrix) {
  let n = matrix.length;
  for (let layer = 0; layer < n / 2; layer++) {
    let first = layer;
    let last = n - 1 - layer;
    for (let i = first; i < last; i++) {
      let offset = i - first;
      let top = matrix[first][i];
      // left -> top
      matrix[first][i] = matrix[last - offset][first];
      //bottom -> left
      matrix[last - offset][first] = matrix[last][last - offset];
      // right -> bottom
      matrix[last][last - offset] = matrix[i][last];
      // top -> right
      matrix[i][last] = top;
    }
  }
  console.log(matrix)
  console.log('result in alternative solution')
}
var rotateMatrix = function(matrix) {
  var edge = matrix.length - 1;

  var movePixels = function(row, col) {
    // starts at m[row][col]
    // moves to m[col][edge - row]
    var fromRow;
    var fromCol;
    var fromPixel;

    // first transformation
    var toRow = row; // 0
    var toCol = col; // 1
    var toPixel = matrix[row][col];

    // Do rotational transformation 4 times
    for (var i = 0; i < 4; i++) {
      fromRow = toRow;
      fromCol = toCol;
      toRow = fromCol;
      toCol = edge - fromRow;

      fromPixel = toPixel;
      toPixel = matrix[toRow][toCol];
      matrix[toRow][toCol] = fromPixel;
    }
  };

  for (var i = 0; i < matrix.length / 2; i++) {
    for (var j = i; j < edge - i; j++) {
      movePixels(i, j);
    }
  }
};
let testMatrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]


// console.log('before:');
// rotateMatrix(testMatrix);
rotateMatrixAlt(testMatrix);

const res = [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3],
]
