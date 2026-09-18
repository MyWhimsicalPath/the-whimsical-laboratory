let flowers = [];

function setup() {
  let canvas = createCanvas(400, 400);
canvas.parent("canvas-container");
  
  background(20);
  angleMode(DEGREES);
}

function mousePressed() {
  if (
    mouseX >= 0 && mouseX < width &&
    mouseY >= 0 && mouseY < height
  ) {
    flowers.push({
  x: mouseX,
  y: mouseY,
  petals: Number(document.getElementById("petal-range").value),
  size: random(20, 50),
  angle: random(360),
  opacity: 255
});

    

    drawFlower(mouseX, mouseY);
  }
}

function drawFlower(x, y) {
  let petals = Number(
  document.getElementById("petal-range").value
);
  let size = random(20, 50);

  push();
  translate(x, y);
  rotate(random(360));

  noStroke();
  fill(150, 175, 125, 80);

  for (let i = 0; i < petals; i++) {
    ellipse(0, size / 3, size / 3, size);
    rotate(360 / petals);
  }

  fill(210, 185, 100);
  circle(0, 0, size / 4);

  pop();
}

function clearArchive() {
  flowers = [];
  background(20);
}
