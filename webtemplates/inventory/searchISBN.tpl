<!DOCTYPE html>
<html>

    <body>
        <div>
            <form id="isbnSearchForm" action="/searchISBN/" method="GET">
                ISBN: <input type="text" name="ISBN"/>
                <input type="submit" value="Search" name="isbnSearchButton"/>
            </form>
        </div><br/>

        % if srch_results:
            <div style="border: 1px solid black;">
                {{srch_results}}
            </div>
            <br/>
            <div style="border: 1px solid black;">
                <p>Title: {{srch_results['title'] + (' - ' + srch_results['subtitle'] if srch_results['subtitle'] else '')}} <br/></p>
                % if srch_results['imageLinks']:
                    <img src="{{srch_results['imageLinks']['smallThumbnail']}}"/>
                    <br/>
                % end
                <p>Description: {{srch_results['description'] if 'description' in srch_results else 'no description'}}</p>
            </div>
        % else:
            <div>
                <h2>No results to display!</h2>
            </div>
        % end
    </body>

</html>
