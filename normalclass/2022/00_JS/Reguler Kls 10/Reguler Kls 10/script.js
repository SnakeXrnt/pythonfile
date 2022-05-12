document.addEventListener('DOMContentLoaded', () => {

	let canvas = document.getElementById("canvas");
	let ctx = canvas.getContext("2d");


	const blockSize = 20

	const startButton = {
		x : canvas.width/6,
		y : canvas.height/3,
		width : 8 * blockSize,
		height : 3 * blockSize,
		color : "#fcff4f",
		textColor : "Black",
		font : "32px Courier Bold",
		align : "center",
		baseline : "middle",

		draw : function (){
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x - this.width/2, this.y - this.height/2, this.width, this.height);

			ctx.fillStyle = this.textColor;
			ctx.font = this.font;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText('Start', this.x, this.y);
		},

		checkClicked : function (event){
			if ((event.offsetX >= this.x - this.width/2) && (event.offsetY >= this.y- this.height/2) && (event.offsetX <= (this.x + this.width/2)) && (event.offsetY <= (this.y + this.height/2))){
				console.log("Start")
			};
		}

	}

	document.querySelector("#canvas").addEventListener('click', function(event){
		startButton.checkClicked(event);
	
	})

	const playButton = {
		x : canvas.width/6,
		y : canvas.height/2,
		width : 8 * blockSize,
		height : 3 * blockSize,
		color : "#fcff4f",
		textColor : "Black",
		font : "32px Courier Bold",
		align : "center",
		baseline : "middle",

		draw : function (){
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x - this.width/2, this.y - this.height/2, this.width, this.height);

			ctx.fillStyle = this.textColor;
			ctx.font = this.font;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText('Play', this.x, this.y);
		},

		checkClicked : function (event){
			if ((event.offsetX >= this.x - this.width/2) && (event.offsetY >= this.y- this.height/2) && (event.offsetX <= (this.x + this.width/2)) && (event.offsetY <= (this.y + this.height/2))){
				console.log("Play")
			};
		}

	}


	document.querySelector("#canvas").addEventListener('click', function(event){
		playButton.checkClicked(event);
	
	})	

	const exitButton = {
		x : canvas.width/6,
		y : canvas.height/1.5,
		width : 8 * blockSize,
		height : 3 * blockSize,
		color : "#fcff4f",
		textColor : "Black",
		font : "32px Courier Bold",
		align : "center",
		baseline : "middle",

		draw : function (){
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x - this.width/2, this.y - this.height/2, this.width, this.height);

			ctx.fillStyle = this.textColor;
			ctx.font = this.font;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText('Exit', this.x, this.y);
		},

		checkClicked : function (event){
			if ((event.offsetX >= this.x - this.width/2) && (event.offsetY >= this.y- this.height/2) && (event.offsetX <= (this.x + this.width/2)) && (event.offsetY <= (this.y + this.height/2))){
				console.log("Exit")
			};
		}

	}
	
	document.querySelector("#canvas").addEventListener('click', function(event){
		exitButton.checkClicked(event);
	
	})	

	const music = new Audio('music.mp3');

	let mainloop = setInterval( () => {
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		startButton.draw();
		playButton.draw();
		exitButton.draw();

		music.play();
		music.loop = true;

	})

})