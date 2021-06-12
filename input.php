<?php
ini_set("max_execution_time", "120");
$interests=$_POST['interests'];
$result=array();
$runresult;
exec("python .\client.py $interests", $result,$runresult);
$result=$result[0];
$result=explode(",",$result);
if(count($result)<3){
	header('Location: error.html');
	exit();
}
?>

<!DOCTYPE html>
<html lang="zxx" class="no-js">

<script>
    function input_info() {
        var interests = document.getElementById("interests");
    }
</script>

<head>
    <!-- Mobile Specific Meta -->
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Favicon-->
    <link rel="shortcut icon" href="img/fav.png">
    <!-- Author Meta -->
    <meta name="author" content="codepixer">
    <!-- Meta Description -->
    <meta name="description" content="">
    <!-- Meta Keyword -->
    <meta name="keywords" content="">
    <!-- meta character set -->
    <meta charset="UTF-8">
    <!-- Site Title -->
    <title>Home</title>

    <!--
			Google Font
			============================================= -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,500,600" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500i" rel="stylesheet">

    <!--
			CSS
			============================================= -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css">
    <link rel="stylesheet" href="css/linearicons.css">
    <link rel="stylesheet" href="css/font-awesome.min.css">
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/magnific-popup.css">
    <link rel="stylesheet" href="css/nice-select.css">
    <link rel="stylesheet" href="css/animate.min.css">
    <link rel="stylesheet" href="css/owl.carousel.css">
    <link rel="stylesheet" href="css/main.css">
</head>

<body>

    <!-- Start Header Area -->
    <header id="header">
        <div class="container">
            <div class="row align-items-center justify-content-between d-flex">
                <div id="logo">
                    <a href="index.html"><img src="img/logo.png" alt="" title="" /></a>
                </div>
                <nav id="nav-menu-container">
                    <ul class="nav-menu">
                        <li class="menu-active"><a href="index.html">Home</a></li>
                    </ul>
                </nav>
                <!-- #nav-menu-container -->
            </div>
        </div>
    </header>
    <!-- End Header Area -->


    <!-- Start Banner Area -->
    <section class="home-banner-area relative">
        <div class="container">
            <div class="row justify-content-center">
                <div class="banner-content col-lg-8 col-md-12">
                    <div class="section-title text-center">
                        <h1>Recommended Faculties</h1>
                        <p>
                            These are the recommended faculties from our database whose interests match yours a lot.
                        </p>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center d-flex align-items-center">
                <div class="col-lg-3 col-md-6 col-sm-12 single-faculty">
                    <div class="thumb d-flex justify-content-center">
						<?php  echo "<img class=\"img-fluid\" src=\"img/faculty/$result[0].jpg\" >" ?>
                    </div>
                    <div class="meta-text text-center">
                        <h4><?php echo $result[0];?></h4>
                        <!--p class="designation">Director,Theoretical</p-->
                        <div class="info wow fadeIn" data-wow-duration="1s" data-wow-delay=".1s">
                            <p>
                                Match Score: <br /><?php echo $result[1];?><br />
                            </p>
                        </div>
                        <div class="align-items-center justify-content-center d-flex">
                            <a href=<?php echo $result[2];?>><i class="fa fa-facebook"></i></a>
                            <a href="#"><i class="fa fa-twitter"></i></a>
                            <a href="#"><i class="fa fa-linkedin"></i></a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-12 single-faculty">
                    <div class="thumb d-flex justify-content-center">
						<?php  echo "<img class=\"img-fluid\" src=\"img/faculty/$result[3].jpg\" >" ?>
                    </div>
                    <div class="meta-text text-center">
                        <h4><?php echo $result[3];?></h4>
                        <!--p class="designation">Director,Theoretical</p-->
                        <div class="info wow fadeIn" data-wow-duration="1s" data-wow-delay=".1s">
                            <p>
                                Match Score: <br /><?php echo $result[4];?><br />
                            </p>
                        </div>
                        <div class="align-items-center justify-content-center d-flex">
                            <a href=<?php echo $result[5];?>><i class="fa fa-facebook"></i></a>
                            <a href="#"><i class="fa fa-twitter"></i></a>
                            <a href="#"><i class="fa fa-linkedin"></i></a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-12 single-faculty">
                    <div class="thumb d-flex justify-content-center">
						<?php  echo "<img class=\"img-fluid\" src=\"img/faculty/$result[6].jpg\" >" ?>
                    </div>
                    <div class="meta-text text-center">
                        <h4><?php echo $result[6];?></h4>
                        <!--p class="designation">Director,Theoretical</p-->
                        <div class="info wow fadeIn" data-wow-duration="1s" data-wow-delay=".1s">
                            <p>
                                Match Score: <br /> <?php echo $result[7];?><br />
                            </p>
                        </div>
                        <div class="align-items-center justify-content-center d-flex">
                            <a href=<?php echo $result[8];?>><i class="fa fa-facebook"></i></a>
                            <a href="#"><i class="fa fa-twitter"></i></a>
                            <a href="#"><i class="fa fa-linkedin"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Banner Area -->    

    <!-- ####################### Start Scroll to Top Area ####################### -->
    <div id="back-top">
        <a title="Go to Top" href="#"></a>
    </div>
    <!-- ####################### End Scroll to Top Area ####################### -->

    <script src="js/vendor/jquery-2.2.4.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/vendor/bootstrap.min.js"></script>
    <!---<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBhOdIF3Y9382fqJYt5I_sswSrEw5eihAA"></script>--->
    <script src="js/easing.min.js"></script>
    <script src="js/hoverIntent.js"></script>
    <script src="js/superfish.min.js"></script>
    <script src="js/jquery.ajaxchimp.min.js"></script>
    <script src="js/jquery.magnific-popup.min.js"></script>
    <script src="js/owl.carousel.min.js"></script>
    <script src="js/owl-carousel-thumb.min.js"></script>
    <script src="js/jquery.sticky.js"></script>
    <script src="js/jquery.nice-select.min.js"></script>
    <script src="js/parallax.min.js"></script>
    <script src="js/waypoints.min.js"></script>
    <script src="js/wow.min.js"></script>
    <script src="js/jquery.counterup.min.js"></script>
    <script src="js/mail-script.js"></script>
    <script src="js/main.js"></script>
</body>

</html>