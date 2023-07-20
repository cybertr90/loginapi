<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
<form action="/register" method = "POST">
        <label for="username">Username</label>
        <input type="text" name = "username">
        <label for="password">Password</label>
        <input type="password" name = "password">
        <input type="submit" value = "Register">
        
    </form>
     <br>
    <a href="{{url_for('home')}}">Home</a>
    
</body>
</html>