function lock(val) {
	var lock = document.getElementById("lock");
	var unlock = document.getElementById("unlock");
	lock.id = "unlock";
	unlock.id = "lock";
	if (val == 0){		
			$.post(                             //call the server
		"unlock.php",                     //At this url
		{
			field: "value",
			name: "John"
		}                               //And send this data to it
		).done(                             //And when it's done
			function(data)
			{
				$('#fromAjax').html(data);  //Update here with the response
			}
		);
	}
	
	if (val == 1){
		$.post(                             //call the server
		"lock.php",                     //At this url
		{
			field: "value",
			name: "John"
		}                               //And send this data to it
		).done(                             //And when it's done
			function(data)
			{
				$('#fromAjax').html(data);  //Update here with the response
			}
		);
	}
}	
