<p>Login</p>
<form action="/login" method="POST">
<<<<<<< HEAD
   User Name: <input type="text" size="100" maxlength="100" name="username"/><br>
   Password:  <input type="text" size="100" maxlength="100" name="password"/><br>
   <hr>
   Token:  <input type="text" size="100" maxlength="100" name="crsf_token" value="{{crsf_token}}"/><br>
   <hr>
=======
    User Name: <input type="text" size="100" maxlength="100" name="username"/><br>
    Password:  <input type="text" size="100" maxlength="100" name="password"/><br>
    <hr>
    Token: <input type="text" size="100" maxlength="100" name="csrf_token" value="{{csrf_token}}"/><br>
    <hr>
>>>>>>> b2693012a90410afe5705293c2236191d9d3b702
    <input type="submit" name="login" value="Login"/>
</form>