<!DOCTYPE html>
<html>

<header>

    <form action="../../credentialhandler" method="POST" align="right">
        % if this_user:
            <input type="submit" name="logout" value="Logout {{this_user.nickname()}}"/>
        % else:
            <input type="submit" name="login" value="Login"/>
        % end
            <input type="hidden" name="redirectTarget" value="{{redirect_path}}">
    </form>

</header>

<body>
    <div>
        <form action="/guestbook/" method="GET">
            <input type="submit" name="signButton" value="Sign The Guestbook"/>
        </form><br/><br>
    </div>

    <div>
        <form name="filterAction" action="." method="POST">
            <input type="text" name="filterText"/>
            <input type="submit" name="filterButton" value="Search Author"/>
        </form> <br/>
    </div>

    % if fetch_results:
        % for result in fetch_results:
            <div style="border: 1px solid black;">
                <b>Date:</b> {{result.time_added}}<br/>
                <b>Author:</b> {{result.comment_author}} <br/>
                <b>Comment:</b> <p>{{result.comment}}</p>
            </div> <br/>
        % end
    % else:
        <h2>No guest books signatures fetched!</h2>
    % end

</body>


</html>