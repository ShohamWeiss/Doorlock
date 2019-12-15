<?php
$username = $_POST['user']; //Gets the user pass from the post
$pass = $_POST['pass'];

$output = shell_exec("python login.py $username $pass"); // Forwards to python script
if ($output == "correct\n") { // forwards back if they are correct or not
	echo 1;
} else {
	echo 0;
}
?>
