<?php

$url = file_get_contents('https://api.kawalcorona.com/indonesia/');
$data = json_decode($url,true);

echo "Negara : " . $data[0]['name'] . "<br>";
echo "Positif : " . $data[0]['positif'] . " Orang <br>";
echo "Sembuh : " . $data[0]['sembuh'] . " Orang <br>";
echo "Meninggal : " . $data[0]['meninggal'] . " Orang <br>";

?>
