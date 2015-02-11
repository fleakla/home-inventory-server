<html>

<body>
    <div id="wrap">

        <form action="/saveFormTest" method="POST">
            Title: <br /> <input type="text" name="title"/> <br/>
            Genre: <br/> <select name="genre">
                            <option value="fiction">Fiction</option>
                            <option value="non-fiction">Non-Fiction</option>
                         </select>
                    <br/>
            Author: <br/> <input type="text" name="author"> <br/>
            <input type="submit" value="Save">
        </form>

    </div>
</body>


</html>