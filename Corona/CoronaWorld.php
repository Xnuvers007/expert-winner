<?php
$url = file_get_contents('https://api.kawalcorona.com/positif');
$url1 = file_get_contents('https://api.kawalcorona.com/sembuh');
$url2 = file_get_contents('https://api.kawalcorona.com/meninggal');

$data = json_decode($url,true);
$data1 = json_decode($url1,true);
$data2 = json_decode($url2,true);

echo "Total Positif : " . $data[0]['name'] . "\n";
echo "Positif : ". $data[0]['value'] . "\n";

echo "Total Sembuh : " . $data1[0]['nama'] . "\n";
echo "Sembuh : ". $data1[0]['value'] . "\n";

echo "Total Meninggal : " . $data2[0]['namae'] . "\n";
echo "Meninggal : ". $data2[0]['value'] . "\n";


?>
