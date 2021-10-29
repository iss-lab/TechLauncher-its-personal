<template>
    <header>
       <nav id="navbar">
         <h1 class="logo"><a href="/">ISS</a></h1>
         <ul>
           <li><a href="/">Home</a></li>
           <li><a href="about.html">About</a></li>
           <li><a href="https://github.com/TechLauncher-its-personal/Personal-Virtual-Assistant-for-News-Filtering">Docs</a></li>
           <li><a v-on:click="almondLogin()">Sign in</a></li>
         </ul>
       </nav>
    </header>
</template>

<script>
export default {
    methods: {
    almondLogin: function() {
      console.log("Login using Almond");
      const url = "https://almond.stanford.edu/me/api/oauth2/authorize?"
                    + "response_type=code"
                    + "&client_id=f79d32042f46485a"
                    + "&redirect_uri=https://its-personal-web.herokuapp.com/almond_auth"
                    + "&scope=profile user-read user-read-results user-exec-command developer-read";
      location.href = url;
    }
  }
}
</script>

<style>
/* Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Main styling */
html,body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.7em;
}

a {
    color:#333;
    text-decoration: none;
}

h1,h2,h3 {
    padding-bottom: 20px;
}

p{
    margin: 10px 0;
}

/*Utility*/
.container{
    margin:auto;
    max-width: 1100px;
    overflow: auto;
    padding: 0 20px; 
}

.text-primary{
    color:#eca072;
}

.lead{
    font-size: 20px;
}

.btn{
    display: inline-block;
    font-size: 18px;
    color: #fff;
    background: #003366;
    padding: 13px 20px;
    margin-right: 50px;
    border: none;
}

.btn:hover{
    background: #eca072;
    color: #003366;
    opacity: 0.9;
}

.bg-primary{
    background: #eca072;
    color: #fff;
}

.bg-light{
    background:#2f9fe3;
    color:#fff;
}

.clr{
    clear: both;
}

/* Navbar */
#navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color:#66A3FA;
    color:#fff;
    opacity: 0.7;
    width: 100%;
    height: 70px;
    top: 0px;
    padding:0 30px;
    transition: 0.5s;
}

#navbar a{
    color:#828282;
}

#navbar h1{
    float:left;
    padding-top: 20px;
    padding-left: 20px;
}

#navbar ul{
    list-style: none;
    float: right;
}

#navbar ul li{
    float: left;
}

#navbar ul li a{
    display: block;
    padding: 20px;
    text-align: center;
}

#navbar ul li a:hover{
    border-bottom:#eca072 2px solid;
}
</style>
