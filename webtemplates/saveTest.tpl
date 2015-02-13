<html>

    <body>

        <div id="bookData">
            <table border="1">
                <tr>
                    % for key in sorted(dataDictionary.keys()):
                    <td>
                       <h1>{{key}}</h1>
                    </td>
                    % end
                </tr>

                <tr>
                    % for k2 in sorted(dataDictionary.keys()):
                    <td>
                        {{dataDictionary[k2]}}
                    </td>
                    % end
                </tr>
            </table>
        </div>

    </body>

</html>