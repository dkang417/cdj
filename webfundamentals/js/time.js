
<!DOCTYPE html>
<html>
<head>
	<title>If You Dont Mind, Can i Have The Time</title>
	<script type="text/javascript">
		var HOUR = 8;
		var MINUTE = 50;
		var PERIOD = "AM";

		var str = "Its ";

		if (MINUTE > 30) {
			str += "almost" + (HOUR + 1)
		} else{
			str += "just after" + HOUR
		}


		if(PERIOD == "PM"){
			str += "in the evening."
		} else {
			str += "in the morning."
		}

		console.log(str);
		</script>
</head>
<body>
</body>
</html>
