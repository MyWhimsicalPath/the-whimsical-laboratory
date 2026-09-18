let flowers = [];

function setup() {
  let canvas = createCanvas(400, 400);
canvas.parent("canvas-container");
  
  background(20);
  angleMode(DEGREES);
}

function draw() {
  background(20);

  for (let flower of flowers) {
    flower.opacity = max(
      0,
      flower.opacity - 25 * deltaTime / 1000
    );

    drawFlower(flower);
  }

  flowers = flowers.filter(flower => flower.opacity > 0);
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

function drawFlower(flower) {
  push();
  translate(flower.x, flower.y);
  rotate(flower.angle);

  noStroke();
  fill(150, 175, 125, flower.opacity * 80 / 255);

  for (let i = 0; i < flower.petals; i++) {
    ellipse(
      0,
      flower.size / 3,
      flower.size / 3,
      flower.size
    );
    rotate(360 / flower.petals);
  }

  fill(210, 185, 100, flower.opacity);
  circle(0, 0, flower.size / 4);

  pop();
}

function clearArchive() {
  flowers = [];
  background(20);
}
