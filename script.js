$(document).ready(function(){
	// When the page loads, check if the user has the coookies to access the lock/ unlock interface or needs to login.
	document.getElementById("load").hidden = true;
	$.get('access.php', function(data) {
		if (data == 0) { // The user doesn't have access
			document.getElementById("lock").hidden = true; //hide lock/unlock
			document.getElementById("unlock").hidden = true;
			document.getElementById("load").hidden = true;
			document.getElementById("login").hidden = false; //show login
			document.getElementById("username").hidden = false;
			document.getElementById("password").hidden = false;
		}
		if (data == 1) { //has access
			document.getElementById("login").hidden = true; //hide lock/unlock
			document.getElementById("username").hidden = true;
			document.getElementById("password").hidden = true;
			statusupdate(); //update lock/unlock depending on the status
		}
	});
});

function lock() {
	load(); // show loading animation
	$.get('lock.php', function(data) { //send a request to lock.php
		document.getElementById("lock").hidden = true; // show the unlock button only
		document.getElementById("unlock").hidden = false;
	});
}

function unlock() {
	load(); // show loading animation
	$.get('unlock.php', function(data) { //send a request to lock.php
		document.getElementById("lock").hidden = false;// show the lock button only
		document.getElementById("unlock").hidden = true;
	});
}

function login() {
	var username = document.getElementById("username").value; // get username and password from the user
	var password = document.getElementById("password").value;
	document.getElementById("username").style.border = "2px solid black";
	document.getElementById("password").style.border = "2px solid black";
	
	$.post('login.php', {user : username, pass : password}, function(data) { // Send user pass to check with database
		if (data == 1) { // The user pass is correct
			document.getElementById("login").hidden = true;
			document.getElementById("username").hidden = true;
			document.getElementById("password").hidden = true;
			statusupdate(); // Show lock/ unlock depending on the status
		}
		if (data == 0) {// The user pass is incorrect
			document.getElementById("username").style.border = "2px solid #f44336"; //Add red border
			document.getElementById("password").style.border = "2px solid #f44336";
		}
	});	
}

function statusupdate() { // When we move to lock/ unlock interface
	$.post('status.php', function(data) { // Call to see if the door is currently locked/ unlocked
		if (data == 1) { // If unlocked
			document.getElementById("lock").hidden = false; // Show lock button
			document.getElementById("unlock").hidden = true;
		}
		if (data == 0) { // If locked
			document.getElementById("lock").hidden = true; // Show unlock button
			document.getElementById("unlock").hidden = false;
		}
		});
}

// Under here is just the loading animation (Cosmetics)
const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
}

const load = async () => {
	document.getElementById("load").hidden = false;
	await sleep(1300)
	document.getElementById("load").hidden = true;
}
