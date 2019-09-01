/**
*  --------------------------------------------------------------------
*  | This webpage is a fully interactive pixel art maker!  The user   |
*  | can select the size of canvas (grid) that they would like to use.|
*  | They can then select a color through a color picker. By clicking |
*  | on the individual cells they can change the background color to  |
*  | whatever color they selected. Descriptions of each code block    |
*  | are listed above the block they describe. Please enjoy!      ~Cam|
*  --------------------------------------------------------------------
*/

/**
* @description- Function takes user generated input and assigns it
*               to a variable to be used in makeGrid() function.
* @constructor 
* @param {string} - height: user generated from <input> boxes
* @param {string} - width: user generated from <input> boxes
*/
function getHeightWidth() {
    event.preventDefault();
    let height = document.getElementById('inputHeight').value;
    let width = document.getElementById('inputWidth').value;
    makeGrid(height, width);
}

/**
* @description Function draws a grid under teh <table> tag.
*              Two nested for loops do the keep track of the grid,
*              innerHTML executes the actual construction.
* @constructor
* @param {number} height: user generated number passed from
*                 getHeightWidth()
* @param {number} width: user generated number passed from 
*                 getHeightWidth()
* @param {string} grid: where rows and columns for the grid are saved.
* @param {string} canvas: blank <table> where the grid lives
* @returns a grid of the users desierd size
*/
function makeGrid(height, width) {
  let canvas = document.getElementById('pixelCanvas');
  let grid = "";
  
  for(let h = 0; h < height; h++) {
    grid += '<tr class="row-' + h + '\">';    
    for(let w = 0; w < width; w++) {
      grid += '<td class="cell" id="row-' + h + '_cell-' + w + '\"></td>';
    }
    grid += '</tr>';
  }
  canvas.innerHTML = grid;
}

/**
* @description Function that changes the background color of the cell
*              the user clicks in. Called by event listener at bottom 
*              of page.
* @constructor
* @param {string} color: user picked color from <input type="color">
*                        stored in Hex form "#xxxxxx"
* @param {string} theCell: defined in .addEventListener as the first
*                          path of users 'click'.
* @return a specific cell with the background color of users choice
*/
function getColor() {
  let color = document.getElementById('colorPicker').value;
  theCell.style.backgroundColor = color;
}

/**
* @description a default begining grid when page loads
* @param {number} height of grid
* @param {number} width of grid
*/
makeGrid(20, 20);

/**
* @description definition of global variable, theCell, which will
*              be used in later blocks of code
*/
let theCell;

/**
* @description calls function getHeightWidth after user enters their
*              desired height and width then hits submit
*/
document.getElementById('sizePicker').onsubmit = function() {
  getHeightWidth();
};

/**
* @description calls function, getColor, to change the background color
*              of the specific cell that the user has clicked on.
*/
document.addEventListener('click', function(e) {
  theCell = e.path[0];
  if(theCell.nodeName === "TD") {
    getColor(); 
  }
});