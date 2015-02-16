<html>

<header>
    <form action="../credentialhandler" method="POST">
        % if this_user:
            <input type="submit" name="logout" value="Logout {{this_user.nickname()}}"/>
        % else:
            <input type="submit" name="login" value="Login"/>
        % end
            <input type="hidden" name="redirectTarget" value="/tests/">
    </form>
</header>

<body>

    % if this_user:
        <h2>Welcome to our tests {{this_user.nickname()}}</h2>
    % else:
        <h2>Please press the button above to login!</h2>
    % end

</body>


</html>