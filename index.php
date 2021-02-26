<?php
$fileurl = $_GET["url"];
$url = shell_exec('python3 test.py '.$fileurl);
header('Content-Type: video/mp4');
readfile('yiff.mp4');
exit;
?>
