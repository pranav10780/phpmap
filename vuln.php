<?php
if (isset($_GET['ip'])) {
    $ip = $_GET['ip'];
    $cmd = "ping -c 2 " . $ip;
    echo "<pre>Command: $cmd\n\n";
    system($cmd);
    echo "</pre>";
} else {
    echo '<form method="GET">
            Enter IP to ping: <input type="text" name="ip">
            <input type="submit" value="Ping">
          </form>';
}
?>
