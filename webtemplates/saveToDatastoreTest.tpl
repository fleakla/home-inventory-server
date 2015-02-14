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

</html>