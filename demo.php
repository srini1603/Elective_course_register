<?php

$json = file_get_contents('php://input');

// Converts it into a PHP object
$data = json_decode($json);

echo $data[0];

?>


