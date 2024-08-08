const gridContainer = document.getElementById('grid-container');
const colorButtons = document.querySelectorAll('.color-btn');
let selectedColor = '#0000ff'; // Default color is blue

// Create 9x9 grid
for (let i = 0; i < 99*99; i++) {
    const gridItem = document.createElement('div');
    gridItem.classList.add('grid-item');
    gridContainer.appendChild(gridItem);
}

// Add click event listener to each grid item
const gridItems = document.querySelectorAll('.grid-item');
gridItems.forEach((item) => {
    item.addEventListener('click', () => {
        item.style.backgroundColor = selectedColor;
    });
});

// Add click event listener to color buttons
colorButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
        selectedColor = btn.dataset.color;
    });
});
