<?php


$tukhoa = ["Socks", "Tee", "Shoes", "Shorts", "Hoodie", "Cap", "Pants", "Slides", "Tank Top", "Bra", "Ball", "Bag", "Tights", "Dress", "Jacket", "Sunglasses", "Hat", "Suit","Sandals","Backpack","Vest","Sweatshirt","Bikini"];


$ten_tap_tin_goc = 'preprocessed_data.csv';
$ten_tap_tin_moi = 'provip.csv';

// Mở tệp CSV để đọc
$handle_goc = fopen($ten_tap_tin_goc, 'r');

if ($handle_goc === false) {
    die('Không thể mở tệp CSV.');
}

// Mở tệp CSV mới để ghi
$handle_moi = fopen($ten_tap_tin_moi, 'w');


$hang_tieu_de = fgetcsv($handle_goc);
array_push($hang_tieu_de, 'category');
fputcsv($handle_moi, $hang_tieu_de);


while (($row = fgetcsv($handle_goc)) !== false) {
   
    $nameValue = strtolower($row[1]); 
    $url =strtolower($row[9]);
   
    $categoryValue = 'Other'; 
    foreach ($tukhoa as $keyword) {
        $keywordLower = strtolower($keyword);
        if (strpos($nameValue, $keywordLower) !== false) {
            $categoryValue = $keyword;
            break; 
        }
    }
    foreach ($tukhoa as $keyword) {
        $keywordLower = strtolower($keyword);
        if (strpos($url, $keywordLower) !== false) {
            $categoryValue = $keyword;
            break; 
        }
    }
    
    array_push($row, $categoryValue);
    fputcsv($handle_moi, $row);
}


fclose($handle_goc);
fclose($handle_moi);

echo 'Đã thêm trường category vào tệp mới.';

?>
