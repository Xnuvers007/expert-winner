<?php

$url = file_get_contents('https://api.kawalcorona.com/indonesia/provinsi');
$data = json_decode($url,true);

foreach($data as $d)
{
  echo $d['attributes']['FID'];
  echo "\n";
}

echo "\n";

echo "FID : " . $data[0]['attributes']['FID'] . "\n";

echo "Kode Provinsi : " . $data[0]['attributes']['Kode_Provi'] .  "\n";

echo "Provinsi : " . $data[0]['attributes']['Provinsi'] . "\n";

echo "Positif : " . $data[0]['attributes']['Kasus_Posi'] . " Orang\n";
echo "Sembuh : " . $data[0]['attributes']['Kasus_Semb'] . " Orang\n";
echo "Meninggal : ". $data[0]['attributes']['Kasus_Meni'] . " Orang\n";

?>
