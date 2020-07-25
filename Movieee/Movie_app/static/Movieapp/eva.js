function index_validation() 
{
    var user = document.getElementById('user').value;
    var pass = document.getElementById('password').value;

    if (user == "") 
    {
         document.getElementById('username').innerHTML = "**Please fill the username";
         return false;
    }
    if (pass == "") 
    {
         document.getElementById('pass').innerHTML = "**Please fill the password";
         return false;
    }

}

function register_validation()
{
   var x = document.getElementById('name').value;
   var name = document.getElementById('lname').value;
   var email = document.getElementById('email').value;
   var user = document.getElementById('user').value;
   var pass = document.getElementById('password').value;
   var repass = document.getElementById('repassword').value;

       if (x == "") 
        {
          document.getElementById('f1name').innerHTML = "**Please fill the first name";
          return false;
        }

       if (name == "") 
        {
          document.getElementById('l1name').innerHTML = "**Please fill the last name";
          return false;
        }

       if (email == "") 
        {
           document.getElementById('emailid').innerHTML = "**Please fill the email id";
           return false;
        }
       if (user == "") 
        {
            document.getElementById('username').innerHTML = "**Please fill the username";
            return false;
        }

       if (pass == "") 
        {
            document.getElementById('pass').innerHTML = "**Please fill the password";
            return false;
        }

      
       if (repass == "") 
        {
            document.getElementById('repass').innerHTML = "**Renter the password";
             return false;
        }

}