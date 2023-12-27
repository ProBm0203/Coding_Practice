<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $name = $_POST["Name"] ?? ""; // Get the entered name
    $address = $_POST["address"] ?? ""; // Get the entered address
    $selectedSports = $_POST["sports"] ?? []; // Get an array of selected sports (if any)
    $gender = $_POST["gender"] ?? ""; // Get the selected gender

    // Display the submitted information
    echo "<h2>Submitted Information:</h2>";
    echo "<p>Name: $name</p>";
    echo "<p>Address: $address</p>";
    echo "<p>Selected Sports:</p>";
    echo "<ul>";
    foreach ($selectedSports as $sport) {
        echo "<li>$sport</li>";
    }
    echo "</ul>";
    echo "<p>Gender: $gender</p>";

    // Process other form fields as needed...
    // For example, handling file uploads, validating data, storing in a database, etc.
}
?>
