<?php
$date_of_expiry = time() + 60 * 60 * 24 * 7; #1 week until cookie will expire
if ($_COOKIE["access"] != "granted") { // If the user doesn't have this cookie
	setcookie( "access", "granted", $date_of_expiry, "/"); // Add the access granted cookie
}
$output = shell_exec("python status.py"); // Check the status of the lock
if ($output == "unlocked\n") { // forward the status of the lock
	echo 1;
} else {
	echo 0;
}
?>
