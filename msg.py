import os
import sys
import time
import getpass

xuser = str(getpass.getuser())
filepath = str('C://Users//'+xuser+'//Desktop//GIFT.hta')
backpath = str('https://github.com/alectramell/msg/raw/master/img/bg.png')
xdata = str('''<font face="arial" color="#29ff34" size="6"><b>MERRY CHRISTMAS!!!</b></font></b><br />from <b>Tramell Software Development!</b><br /><br /><font color="#00c3ff" size="4"><b>90% Off Full-Site Custom Web-Design</b></font><br /><font color="#ffffff" size="3"><b>[coupon-code]:</b> 1234567890</font>''')
xdocument = '''
<HTA:application

	id="webapp"
	border="none"
	innerborder="no"
	scroll="no"
	navigable="yes"
/>
<html>
<head>
<title>
WebApp v1.0
</title>
</head>
<body>

<script type="text/javascript">

	window.moveTo(380, 100);
	window.resizeTo(500, 400);

	function exitApp() {

		setTimeout(function(){window.close()}, 500);
	}

</script>

<style type="text/css">

	body, html {

		background:url('''+backpath+''');
		background-size:cover;
		overflow:hidden;
	}

	#exitButton {

		position:absolute;
		top:5px;
		left:7px;
		font-family:arial;
		font-size:14px;
		color:#4c4c4c;
		text-decoration:bold;
		cursor:pointer;
	}

	#mainText {

		position:absolute;
		top:30px;
		left:20px;
		padding:5px 5px;
		margins:5px 5px;
		font-family:consolas;
		font-size:18px;
		color:#ffffff;
		text-decoration:bold;
		cursor:arrow;
	}

	#facebookLink {

		position:absolute;
		bottom:10px;
		left:157px;
		padding:5px 5px;
		margins:5px 5px;
		font-family:arial;
		font-size:12px;
		color:#ffffff;
		text-decoration:bold;
		underline:none;
		cursor:pointer;
	}

</style>

<font id="exitButton" onclick="exitApp();">close</font>

<font id="mainText">'''+xdata+'''</font>

<a id="facebookLink" href="https://www.facebook.com/tramelldev" target="_new">www.facebook.com/tramelldev</a>

</body>
</html>
'''

xfile = open(filepath, 'w')
xfile.write(xdocument)
xfile.close()

xcom = str('START /min '+filepath)
os.system(xcom)