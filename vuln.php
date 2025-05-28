<?php
if (isset($_GET['ip']) && isset($_GET['name'])) {
    $name = $_GET['name'];
    $ip = $_GET['ip'];
    
    echo "<pre>";
    echo "Name: $name\n\n";
    
    $cmd = "ping -c 2 $ip";
    echo "Command: $cmd\n\n";
    system($cmd);
    echo "</pre>";
} else {
    echo '<form method="GET">
            Name: <input type="text" name="name"><br>
            Enter IP to ping: <input type="text" name="ip"><br>
            <input type="submit" value="Ping">
          </form>';
}
?>

