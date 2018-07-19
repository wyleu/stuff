function setup() {
    var cnv = createCanvas(windowWidth, windowHeight, WEBGL);
    cnv.parent('myContainer');

}

function draw(){
  background(255);
  box();
  translate(100,100,-100);
  box();
  rotateX(radians(45));
  translate(100,100,-100);
  box();
	beginShape();
	vertex(100,23,-100);
	vertex(200,23,-50);
	vertex(150, 45,-100);
	endShape();
}