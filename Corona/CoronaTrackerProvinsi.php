<?php

$url = file_get_contents('https://api.kawalcorona.com/indonesia/provinsi');
$data = json_decode($url,true);

echo "daftar attribut : ".$data[0]['attributes']. "\n";

echo "FID : " . $data[0]['FID'] . "\n";
echo "Kode Provinsi : " . $data[0]['Kode_Provi'] . "\n";
echo "Provinsi : " . $data[0]['Provinsi'] . "\n";
echo "Positif : " . $data[0]['Kasus_Posi'] . " Orang\n";
echo "Sembuh : " . $data[0]['Kasus_Semb'] . "orang\n";
echo "Meninggal : " . $data[0]['Kasus_Meni'] . "orang\n";

?>