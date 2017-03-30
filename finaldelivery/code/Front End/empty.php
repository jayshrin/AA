<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Empty Page</title>
	<!-- Bootstrap Styles-->
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
     <!-- FontAwesome Styles-->
    <link href="assets/css/font-awesome.css" rel="stylesheet" />
        <!-- Custom Styles-->
    <link href="assets/css/custom-styles.css" rel="stylesheet" />
     <!-- Google Fonts-->
   <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />


</head>
<body>
        <!-- /. NAV SIDE  -->
        <!--<div id="page-wrapper" >-->
            <div id="page-inner">
			    <div class="row">
                    <div class="col-md-12">
                        <h1 class="page-header">
                            {{tle}} <small>{{bodyy}}</small>
                        </h1>
                        {{user}}
                    </div>
                </div>
                <div>
             <table style="width:100%">
                        <tr>
                            <th>CLOUD ID</th>
                            <th>NODE ID</th>
                            <th>VM ID</th>
                            <th>CPU</th>
                            <th>RAM</th>
                            <th>STORAGE</th>
                            <th>ACTIVE</th>
                        </tr>
       
<?php
//session_start();
//connect to database
$servername = “localhost”;
$username = "root";
$password = “”;
if (!$link = mysql_connect($servername, $username, $password)) {
    echo 'Could not connect to mysql';
    exit;
}
if (!mysql_select_db('MIAAS', $link)) {
    echo 'Could not select database';
    exit;
}

$sql = "SELECT * FROM vms";
$result = mysql_query($sql);

while($row = mysql_fetch_array($result))
{
echo "<tr>";

    echo "<td>{$row['cloud_id']} </td> ".
         "<td>{$row['node_id']} </td>".
         "<td>{$row['vm_id']}  </td>".
	 "<td>{$row['cpu']}  </td>".
   	 "<td>{$row['ram']}  </td>".
   	 "<td>{$row['storage']}  </td>".
   	 "<td>{$row['active']}  </td>";
echo "</tr>";
} 
echo "</table>";

?>


            		<footer><p>All right reserved. Team: 17</p></footer>
            </div>
             <!-- /. PAGE INNER  -->
            <!--</div>-->
         <!-- /. PAGE WRAPPER  -->
        <!--</div>-->
     <!-- /. WRAPPER  -->
    <!-- JS Scripts-->
    <!-- jQuery Js -->
    <script src="assets/js/jquery-1.10.2.js"></script>
      <!-- Bootstrap Js -->
    <script src="assets/js/bootstrap.min.js"></script>
    <!-- Metis Menu Js -->
    <script src="assets/js/jquery.metisMenu.js"></script>
      <!-- Custom Js -->
    <script src="assets/js/custom-scripts.js"></script>
    
   
</body>
</html>
