<?php
// router per "php -S": la radice di WordPress arriva dalla variabile WPROOT
$root = getenv('WPROOT');
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
if ($path !== '/' && file_exists($root . $path) && !is_dir($root . $path)) return false;
if (is_dir($root . $path) && file_exists($root . rtrim($path, '/') . '/index.php')) { $_SERVER['SCRIPT_NAME'] = rtrim($path, '/') . '/index.php'; require $root . rtrim($path, '/') . '/index.php'; return; }
if (is_dir($root . $path) && file_exists($root . rtrim($path, '/') . '/index.html')) { return false; }
$_SERVER['SCRIPT_NAME'] = '/index.php';
chdir($root);
require $root . '/index.php';
