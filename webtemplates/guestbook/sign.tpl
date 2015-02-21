<html>

<header>
    <form action="../credentialhandler" method="POST" align="right">
        % if this_user:
            <input type="submit" name="logout" value="Logout {{this_user.nickname()}}"/>
        % else:
            <input type="submit" name="login" value="Login"/>
        % end
            <input type="hidden" name="redirectTarget" value="{{redirect_path}}">
    </form>
</header>

<body>

    % if this_user:
        <h2>Enter your message {{this_user.nickname()}}</h2>
        <textarea form="messageform" name="comment">Your message here...</textarea>
        <form id="messageform" action="/guestbook/sign/" method="POST">
            <input type="hidden" name="author" value="{{this_user.nickname()}}"/>
            <input type="submit" name="save" value="Save"/>
        </form>


    % else:
        <h2>Please press the button above to sign the guest book!</h2>
    % end

</body>


</html>