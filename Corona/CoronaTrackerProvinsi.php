<?php

$url = file_get_contents('https://api.kawalcorona.com/indonesia/provinsi');
$data = json_decode($url,true);

foreach($data as $d)
{
  echo $d['attributes']['FID'];
  echo "\n";
}

echo "\n";

echo "FID : ". $_POST['FID'] . $data[0]['attributes']['FID'] . "\n";
echo "Kode Provinsi : " . $_POST['Kode Provinsi'] . $data[0]['attributes']['Kode_Provi'] . "\n";
echo "Provinsi : " . $_POST['Provinsi'] . $data[0]['attributes']['Provinsi'] . "\n";
echo "Positif : " . $_POST['Positif'] . $data[0]['attributes']['Kasus_Posi'] . " Orang\n";
echo "Sembuh : " . $_POST['Sembuh'] . $data[0]['attributes']['Kasus_Semb'] . " Orang\n";
echo "Meninggal : " . $_POST['Meninggal'] . $data[0]['attributes']['Kasus_Meni'] . " Orang\n";

?>
