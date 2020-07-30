<?php
$url = file_get_contents('https://api.kawalcorona.com/positif');
$url1 = file_get_contents('https://api.kawalcorona.com/sembuh');
$url2 = file_get_contents('https://api.kawalcorona.com/meninggal');

$data = json_decode($url,true);
$data1 = json_decode($url1,true);
$data2 = json_decode($url2,true);

echo $data[0]['name'] . "\n";
echo "Positif : ". $data[0]['value'] . "\n";

echo $data1[0]['name'] . "\n";
echo "Sembuh : ". $data1[0]['value'] . "\n";

echo $data2[0]['name'] . "\n";
echo "Meninggal : ". $data2[0]['value'] . "\n";

?>
