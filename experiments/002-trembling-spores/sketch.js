function setup() {
  createCanvas(400, 400);
  background(20);
  noStroke();
}

function draw() {
  fill(170, 190, 150, 35);

  circle(
    mouseX + random(-20, 20),
    mouseY + random(-20, 20),
    random(2, 18)
  );
}
