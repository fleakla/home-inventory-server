<html>
<header>
    <form action="/credentialhandler" method="POST">
        % if user:
            <input type="submit" name="logout" value="Logout {{user.nickname()}}"/>
        % else:
            <input type="submit" name="login" value="Login"/>
        % end
            <input type="hidden" name="redirectTarget" value="/saveToDataStoreTest">
    </form>
</header>

<body>

    <form action="/saveOrSearchBookData" method="POST">

        Author:<input type="text" name="author"/> <br/>
        Title: <input type="text" name="title"/>  <br/>
        Publication Date: <input type="date" name="PubDate"/> <br/>
        ISBN: <input type="text" name="ISBN"/> <br/>

        <input type="submit" name="Save" value="Save"/>
        <input type="submit" name="Search" value="Search"/>
    </form>

</body>

</html>