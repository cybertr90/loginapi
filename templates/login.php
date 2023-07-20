<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>

<form action="/login" method = "POST">
        <label for="username">Username</label>
        <input type="text" name = "username">
        <label for="password">Password</label>
        <input type="password" name = "password">
        <input type="submit" value = "Log in">
        
    </form>
    <br>
    <a href="{{url_for('register')}}">Have not your account ? Click here to register.</a>
</body>
</html>