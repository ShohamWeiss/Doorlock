<?php
if ($_COOKIE["access"] == "granted") { // Sees if the user has the access granted cookie, and forwards the answer
	echo 1;
}
if ($_COOKIE["access"] != "granted") {
	echo 0;
}
?>
