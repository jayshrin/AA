<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Free Bootstrap Admin Template : Dream</title>
    <!-- Bootstrap Styles-->
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
    <!-- FontAwesome Styles-->
    <link href="assets/css/font-awesome.css" rel="stylesheet" />
    <!-- Morris Chart Styles-->
    <link href="assets/js/morris/morris-0.4.3.min.css" rel="stylesheet" />
    <!-- Custom Styles-->
    <link href="assets/css/custom-styles.css" rel="stylesheet" />
    <!-- Google Fonts-->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />
</head>
<body>

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
            <!-- /. ROW  -->
            <div ng-app="nghub">
                <!--<p>Mobile Devices:</p>-->
                <p>Mobile Devices : <input type="text" ng-model="mob" placeholder="Enter number here"></p>
                <p>Test Servers : <input type="text" ng-model="serv" placeholder="Enter number here"></p>
                <p><b>Mobile Devices: {{mob}}</b></p>
                <p><b>Test Servers: {{serv}}</b></p>
                <button onclick="">Connect</button>
            </div>

            <footer><p>All right reserved. Team: 17 </p></footer>
        </div>
        <!-- /. PAGE INNER  -->
   <!-- </div>
    &lt;!&ndash; /. PAGE WRAPPER  &ndash;&gt;
</div>-->
<!-- /. WRAPPER  -->
<!-- JS Scripts-->
<!-- jQuery Js -->
<script src="assets/js/jquery-1.10.2.js"></script>
<!-- Bootstrap Js -->
<script src="assets/js/bootstrap.min.js"></script>
<!-- Metis Menu Js -->
<script src="assets/js/jquery.metisMenu.js"></script>
<!-- Morris Chart Js -->
<script src="assets/js/morris/raphael-2.1.0.min.js"></script>
<script src="assets/js/morris/morris.js"></script>
<!-- Custom Js -->
<script src="assets/js/custom-scripts.js"></script>
<script src= "http://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js"></script>


</body>
</html>
